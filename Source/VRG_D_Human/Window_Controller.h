// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include <Windows/WindowsHWrapper.h>
#include "Window_Controller.generated.h"

UCLASS(Blueprintable, BlueprintType, ClassGroup=(Custom), meta=(BlueprintSpawnableComponent) )
class VRG_D_HUMAN_API UWindow_Controller : public UActorComponent
{
	GENERATED_BODY()

public:	
	// Sets default values for this component's properties
	UWindow_Controller();

protected:
	HWND m_hWnd;

	// Called when the game starts
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;

	UFUNCTION(blueprintcallable, Category = WControll)
	FVector4 GetCurrentWindowRect();

	UFUNCTION(blueprintcallable, Category=WControll)
	void MoveWindow(int PosX, int PosY);

	UFUNCTION(blueprintcallable, Category=WControll)
	void ResizeWindow(int width, int height);

	UFUNCTION(blueprintcallable, Category = WControll)
	FVector2D GetViewportSize();

	UFUNCTION(blueprintcallable, Category = WControll)
	FVector2D GetMouseCursorPosition();
		
};
