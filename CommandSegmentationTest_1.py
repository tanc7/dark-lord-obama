import Evasion
from Evasion import readPayloadTemplate,findIndexValue, commandSegmentationTech,reconstituteLine,reconstitutePayload,template_reverse_shell

payloadNoEncrypt = template_reverse_shell.splitlines()
shuffledPayload = commandSegmentationTech(payloadNoEncrypt)
reconstitutePayload(shuffledPayload)

