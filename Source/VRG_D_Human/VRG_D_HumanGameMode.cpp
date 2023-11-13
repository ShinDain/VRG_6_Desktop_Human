// Copyright Epic Games, Inc. All Rights Reserved.

#include "VRG_D_HumanGameMode.h"
#include "VRG_D_HumanCharacter.h"
#include "UObject/ConstructorHelpers.h"

AVRG_D_HumanGameMode::AVRG_D_HumanGameMode()
{
	// set default pawn class to our Blueprinted character
	/*static ConstructorHelpers::FClassFinder<APawn> PlayerPawnBPClass(TEXT("/Game/ThirdPerson/Blueprints/BP_ThirdPersonCharacter"));
	if (PlayerPawnBPClass.Class != NULL)
	{
		DefaultPawnClass = PlayerPawnBPClass.Class;
	}*/
}
