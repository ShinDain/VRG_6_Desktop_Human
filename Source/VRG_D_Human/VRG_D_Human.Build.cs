// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class VRG_D_Human : ModuleRules
{
	public VRG_D_Human(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

		PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "HeadMountedDisplay", "EnhancedInput" });
	}
}
