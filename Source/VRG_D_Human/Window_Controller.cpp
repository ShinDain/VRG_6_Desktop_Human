// Fill out your copyright notice in the Description page of Project Settings.


#include "Window_Controller.h"

// Sets default values for this component's properties
UWindow_Controller::UWindow_Controller()
{
	// Set this component to be initialized when the game starts, and to be ticked every frame.  You can turn these features
	// off to improve performance if you don't need them.
	PrimaryComponentTick.bCanEverTick = true;

	// ...
}


// Called when the game starts
void UWindow_Controller::BeginPlay()
{
	Super::BeginPlay();

	// ...
	m_hWnd = GetActiveWindow();

}


// Called every frame
void UWindow_Controller::TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
{
	Super::TickComponent(DeltaTime, TickType, ThisTickFunction);

	// ...
}

FVector4 UWindow_Controller::GetCurrentWindowRect()
{
	RECT rect;
	GetWindowRect(m_hWnd, &rect);

	FVector4 out;
	out.X = rect.left;
	out.Y = rect.right;
	out.Z = rect.top;
	out.W = rect.bottom;
	
	return out;
}

void UWindow_Controller::MoveWindow(int x, int y)
{
	RECT rect;
	GetWindowRect(m_hWnd, &rect);

	int width = rect.right - rect.left;
	int height = rect.bottom - rect.top;

	SetWindowPos(m_hWnd, NULL, x, y, width, height, 0);
}

void UWindow_Controller::ResizeWindow(int width, int height)
{
	RECT rect;
	GetWindowRect(m_hWnd, &rect);

	SetWindowPos(m_hWnd, NULL, rect.left, rect.top, width, height, 0);
}

