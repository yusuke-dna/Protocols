import json
import os
import math

metadata = {
    'protocolName': 'PCR Prep',
    'author': 'Nick <ndiehl@opentrons.com>',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.10'
}


def run(ctx):

    [num_samples, vol_dna_buff, vol_a_to_b, p20_type, p20_mount,
     p300_type, p300_mount, vol_dil_to_d, vol_dil_to_e,
     vol_c_to_d, vol_d_to_e] = get_values(  # noqa: F821
        'num_samples', 'vol_dna_buff', 'vol_a_to_b', 'p20_type', 'p20_mount',
        'p300_type', 'p300_mount', 'vol_dil_to_d', 'vol_dil_to_e',
        'vol_c_to_d', 'vol_d_to_e')

    # modules and labware
    plate_a = ctx.load_labware('thermofishernunc_96_wellplate_450ul', '1',
                               'plate A')
    plate_c = ctx.load_labware('thermofishernunc_96_wellplate_450ul', '2',
                               'plate C')
    plate_d = ctx.load_labware('thermofishernunc_96_wellplate_450ul', '3',
                               'plate D')
    tempdeck = ctx.load_module('temperature module gen2', '4')
    tempdeck.set_temperature(37)
    plate_b = tempdeck.load_labware('thermofishernunc_96_aluminumblock_450ul',
                                    'plate B')
    reservoir = ctx.load_labware('nest_12_reservoir_15ml', '5',
                                 'reagent reservoir')
    plate_e = ctx.load_labware('thermofishernunc_96_wellplate_450ul', '6',
                               'plate E')
    final_plate = ctx.load_labware('biorad_96_wellplate_200ul_pcr', '9',
                                   'final Bio-Rad PCR plate')
    tipracks20 = [
        ctx.load_labware('opentrons_96_tiprack_20ul', slot)
        for slot in ['7', '10']]
    tipracks300 = [
        ctx.load_labware('opentrons_96_tiprack_300ul', slot)
        for slot in ['8', '11']]

    # pipettes
    p20 = ctx.load_instrument(p20_type, p20_mount, tip_racks=tipracks20)
    p300 = ctx.load_instrument(p300_type, p300_mount, tip_racks=tipracks300)

    # samples and reagents
    num_cols = math.ceil(num_samples/8)
    dnase = reservoir.wells()[0]
    edta = reservoir.wells()[1]
    dil_buff = reservoir.wells()[2]
    pcr_mix = reservoir.wells()[3]

    tip_log = {val: {} for val in ctx.loaded_instruments.values()}

    tip_track = False

    folder_path = '/data/tip_track'
    tip_file_path = folder_path + '/tip_log.json'
    if tip_track and not ctx.is_simulating():
        if os.path.isfile(tip_file_path):
            with open(tip_file_path) as json_file:
                data = json.load(json_file)
                for pip in tip_log:
                    if pip.name in data:
                        tip_log[pip]['count'] = data[pip.name]
                    else:
                        tip_log[pip]['count'] = 0
        else:
            for pip in tip_log:
                tip_log[pip]['count'] = 0
    else:
        for pip in tip_log:
            tip_log[pip]['count'] = 0

    for pip in tip_log:
        if pip.type == 'multi':
            tip_log[pip]['tips'] = [tip for rack in pip.tip_racks
                                    for tip in rack.rows()[0]]
        else:
            tip_log[pip]['tips'] = [tip for rack in pip.tip_racks
                                    for tip in rack.wells()]
        tip_log[pip]['max'] = len(tip_log[pip]['tips'])

    def _pick_up(pip, loc=None):
        if tip_log[pip]['count'] == tip_log[pip]['max'] and not loc:
            ctx.pause('Replace ' + str(pip.max_volume) + 'µl tipracks before \
resuming.')
            pip.reset_tipracks()
            tip_log[pip]['count'] = 0
        if loc:
            pip.pick_up_tip(loc)
        else:
            pip.pick_up_tip(tip_log[pip]['tips'][tip_log[pip]['count']])
            tip_log[pip]['count'] += 1

    def _get_samples(lw, pip):
        if pip.type == 'multi':
            return lw.rows()[0][:num_cols]
        else:
            return lw.wells()[:num_samples]

    pip = p20 if vol_dna_buff <= 20 else p300
    _pick_up(pip)
    for d in _get_samples(plate_b, pip):
        pip.transfer(vol_dna_buff, dnase, d, new_tip='never')

    pip2 = p20 if vol_a_to_b <= 20 else p300
    if not pip2 == pip:
        pip.drop_tip()
    for s, d in zip(_get_samples(plate_a, pip2), _get_samples(plate_b, pip2)):
        if not pip2.has_tip:
            _pick_up(pip2)
        if vol_a_to_b < pip2.max_volume:
            mix_vol = vol_a_to_b
        else:
            mix_vol = pip2.max_volume
        pip2.transfer(vol_a_to_b, s, d, mix_after=(5, mix_vol),
                      new_tip='never')
        pip2.drop_tip()

    _pick_up(p300)
    for d in _get_samples(plate_c, p300):
        p300.transfer(45, dnase, d, new_tip='never')
    p300.drop_tip()

    for s, d in zip(_get_samples(plate_b, p20), _get_samples(plate_c, p20)):
        _pick_up(p20)
        p20.transfer(5, s, d, mix_after=(5, 15), new_tip='never')
        p20.drop_tip()

    ctx.delay(minutes=60, msg='Holding plate B at 37C for 1hr')
    tempdeck.set_temperature(4)
    ctx.comment('Holding plate B at 4C indefinitely.')

    for d in _get_samples(plate_c, p20):
        _pick_up(p20)
        p20.transfer(5, edta, d, new_tip='never')
        pip.drop_tip()

    pip = p20 if vol_dil_to_d <= 20 else p300
    _pick_up(pip)
    for d in _get_samples(plate_d, pip):
        pip.transfer(vol_dil_to_d, dil_buff, d, new_tip='never')

    pip2 = p20 if vol_dil_to_e <= 20 else p300
    if not pip2 == pip:
        pip.drop_tip()
    for d in _get_samples(plate_e, pip):
        if not pip2.has_tip:
            _pick_up(pip2)
        pip2.transfer(vol_dil_to_e, dil_buff, d, new_tip='never')
    pip2.drop_tip()

    pip = p20 if vol_c_to_d <= 20 else p300
    for s, d in zip(_get_samples(plate_c, pip), _get_samples(plate_d, pip)):
        _pick_up(pip)
        pip.transfer(vol_c_to_d, s, d, mix_after=(5, 15), new_tip='never')
        pip.drop_tip()

    pip = p20 if vol_d_to_e <= 20 else p300
    for s, d in zip(_get_samples(plate_d, pip), _get_samples(plate_e, pip)):
        _pick_up(pip)
        pip.transfer(vol_d_to_e, s, d, mix_after=(5, 15), new_tip='never')
        pip.drop_tip()

    _pick_up(p300)
    for d in _get_samples(final_plate, p300):
        p300.transfer(22.5, pcr_mix, d, new_tip='never')
    p300.drop_tip()

    for s, d in zip(_get_samples(plate_e, p20),
                    _get_samples(final_plate, p20)):
        _pick_up(p20)
        p20.transfer(2.5, s, d, mix_after=(5, 15), new_tip='never')
        p20.drop_tip()

    ctx.comment('Plate is ready for Droplet Generation')

    # track final used tip
    if tip_track and not ctx.is_simulating():
        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)
        data = {pip.name: tip_log[pip]['count'] for pip in tip_log}
        with open(tip_file_path, 'w') as outfile:
            json.dump(data, outfile)
