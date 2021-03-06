import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'trader_mun_1a':
		return

	actor.addSkill('expertise_munition_resource_refinement_2')

	actor.addSkillMod('expertise_resource_quality_increase', 1)

	addAbilities(core, actor, player)

	return

def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'trader_mun_1a':
		return

	actor.removeSkill('expertise_munition_resource_refinement_2')

	actor.removeSkillMod('expertise_resource_quality_increase', 1)

	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):


	return

def removeAbilities(core, actor, player):


	return
