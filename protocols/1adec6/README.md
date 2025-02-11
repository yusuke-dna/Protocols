# Small Molecule Library Prep (Updated)

### Author
[Opentrons](https://opentrons.com/)

## Categories
* Proteins & Proteomics
	* Assay

## Description
**Updated**
This protocol has been updated based on feedback from the user.

This protocol now utilizes the [P20 8-Channel Pipette (GEN2)](https://shop.opentrons.com/collections/ot-2-pipettes/products/8-channel-electronic-pipette) (instead of the P300), uses additional plates, and has modified liquid handling. The steps of this updated version can be found below.

Part 1: [Small Molecule Library Prep](./1adec6)</br>
Part 2: [Seed Cells](./1adec6-2)</br>
Part 3: [Transfer Small Molecules](./1adec6-3)</br>
Part 4: [Transfer Small Molecules - CSV Input](./1adec6-4)</br>
Part 5: [Custom Supernatant Removal](./1adec6-5)</br>
Part 6: [ProcartaPlex Protocol-1](./1adec6-6)</br>
Part 7: [ProcartaPlex Protocol-2](./1adec6-7)</br>

Explanation of complex parameters below:
* **P20-Multi Mount**: Select which mount the P20-Multi Pipette is attached to.
* **Number of Destination Plates**: Select the number of destination plates.

---

### Labware
* [Opentrons 20µL Tipracks](https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-20ul-tips)
* [NEST 12-Well Reservoir, 15mL](https://shop.opentrons.com/collections/verified-labware/products/nest-12-well-reservoir-15-ml)
* SPL 96-Well Cell Culture Plates
* Thermo-Fast 96-Well, Fully Skirted Plates

### Pipettes
* [P20 8-Channel Pipette (GEN2)](https://shop.opentrons.com/collections/ot-2-pipettes/products/8-channel-electronic-pipette)

### Reagents
* DMSO (Column 1 of 12-Well Reservoir)
* PBS (Column 2 of 12-Well Reservoir)

---

### Deck Setup
**Slot 1**: Aliquot Plate 1 (SPL 96-Well Cell Culture Plat)</br>
</br>
**Slot 2**: Aliquot Plate 2 (SPL 96-Well Cell Culture Plate)</br>
</br>
**Slot 3**: Aliquot Plate 3 (SPL 96-Well Cell Culture Plate)</br>
</br>
**Slot 4**: Sample Plate (Thermo-Fast 96-Well, Fully Skirted Plate)</br>
</br>
**Slot 5**: Destination Plate (Thermo-Fast 96-Well, Fully Skirted Plate)</br>
</br>
**Slot 6**: [NEST 12-Well Reservoir, 15mL](https://shop.opentrons.com/collections/verified-labware/products/nest-12-well-reservoir-15-ml)</br>
</br>
**Slot 7**: [Opentrons 20µL Tiprack](https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-20ul-tips)</br>
</br>
**Slot 8**: [Opentrons 20µL Tiprack](https://shop.opentrons.com/collections/opentrons-tips/products/opentrons-20ul-tips)</br>
</br>


### Reagent Setup
1. Load DMSO in **Column 1** of the [NEST 12-Well Reservoir, 15mL](https://shop.opentrons.com/collections/verified-labware/products/nest-12-well-reservoir-15-ml)
2. Load PBS in **Column 2** of the [NEST 12-Well Reservoir, 15mL](https://shop.opentrons.com/collections/verified-labware/products/nest-12-well-reservoir-15-ml)

---

### Protocol Steps
1. Destination plate, [P20 8-Channel Pipette (GEN2)](https://shop.opentrons.com/collections/ot-2-pipettes/products/8-channel-electronic-pipette): Add 10 µl PBS ([NEST 12-Well Reservoir, 15mL](https://shop.opentrons.com/collections/verified-labware/products/nest-12-well-reservoir-15-ml), Row 2) into columns 1-4 rows A-H, column 5 rows A-B (will access new tips for last transfer).
2. Destination plate, [P20 8-Channel Pipette (GEN2)](https://shop.opentrons.com/collections/ot-2-pipettes/products/8-channel-electronic-pipette): Add 20 µl 66% DMSO ([NEST 12-Well Reservoir, 15mL](https://shop.opentrons.com/collections/verified-labware/products/nest-12-well-reservoir-15-ml), Row 1) into columns 6-9 rows A-H, column 10 rows A-B (will access new tips for last transfer).
3. Source plate, [P20 8-Channel Pipette (GEN2)](https://shop.opentrons.com/collections/ot-2-pipettes/products/8-channel-electronic-pipette): Take 20 µl of column 1-4 rows A-H, column 5 rows A-B, and transfer into the destination plate in the same orientation (columns 1-4 rows A-H, column 5 rows A-B). Replace tips between columns.
4. Destination plate, [P20 8-Channel Pipette (GEN2)](https://shop.opentrons.com/collections/ot-2-pipettes/products/8-channel-electronic-pipette): Mix columns 1-4, 5A-B. pipette 20 µl up & down 4 times. Replace tips between columns.
5. Destination plate, [P20 8-Channel Pipette (GEN2)](https://shop.opentrons.com/collections/ot-2-pipettes/products/8-channel-electronic-pipette): Take 10 µl of column 1-4 rows A-H, column 5 rows A-B, and transfer into column 6-9 rows A-H, column 10 rows A-B (column 1->6, 2->7, 3->8, 4->9, 5->10). Replace tips between columns.
6. Destination plate, [P20 8-Channel Pipette (GEN2)](https://shop.opentrons.com/collections/ot-2-pipettes/products/8-channel-electronic-pipette): Mix columns 5-9, 10A-B. pipette 20 µl up & down 4 times. Replace tips between columns.
7. Aliquot the library plate (columns 1-10, rows A-H) into 2-3 empty SPL 96-Well Cell Culture Plates: [P20 8-Channel Pipette (GEN2)](https://shop.opentrons.com/collections/ot-2-pipettes/products/8-channel-electronic-pipette).
- Take 10 µl of column A rows A-H of the prepared library plate and add to
column A rows A-H in empty plate 1
- Take 10 µl of column A rows A-H of the prepared library plate and add to
column A rows A-H in empty plate 2 (if using)
- Take 10 µl of column A rows A-H of the prepared library plate and add to
column A rows A-H in empty plate 3 (if using)
Replace tips and repeat these steps for columns 2-10 (Replace tips between columns)
8. End of the protocol.

### Process
1. Input your protocol parameters above.
2. Download your protocol bundle.
3. Upload your custom labware to the [OT App](https://opentrons.com/ot-app) by navigating to `More` > `Custom Labware` > `Add Labware`, and selecting your labware files (.json extensions), if needed.
4. Upload your protocol file (.py extension) to the [OT App](https://opentrons.com/ot-app) in the `Protocol` tab.
5. Set up your deck according to the deck map.
6. Calibrate your labware, tiprack and pipette using the OT App. For calibration tips, check out our [support articles](https://support.opentrons.com/en/collections/1559720-guide-for-getting-started-with-the-ot-2).
7. Hit 'Run'.

### Additional Notes
If you have any questions about this protocol, please contact the Protocol Development Team by filling out the [Troubleshooting Survey](https://protocol-troubleshooting.paperform.co/).

###### Internal
1adec6
