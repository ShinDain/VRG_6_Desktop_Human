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

	//SetWindowLong(m_hWnd, GWL_STYLE, GetWindowWord(m_hWnd, GWL_STYLE) & ~WS_SIZEBOX);

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

	SetWindowPos(m_hWnd, HWND_TOPMOST, x, y, width, height, 0);
}

void UWindow_Controller::ResizeWindow(int width, int height)
{
	RECT rect;
	GetWindowRect(m_hWnd, &rect);

	SetWindowPos(m_hWnd, HWND_TOPMOST, rect.left, rect.top, width, height, 0);
}

FVector2D UWindow_Controller::GetViewportSize()
{
	FVector2D viewportSize = FVector2D(GEngine->GameViewport->Viewport->GetSizeXY());

	return viewportSize;
}

FVector2D UWindow_Controller::GetMouseCursorPosition()
{
	POINT mousePos;
	GetCursorPos(&mousePos);

	return FVector2D(mousePos.x, mousePos.y);
}

bool UWindow_Controller::CheckKeyboard_F4()
{
	if (GetAsyncKeyState(VK_F4))
	{
		return true;
	}
	return false;
}

bool UWindow_Controller::CheckKeyboard_F8()
{
	if (GetAsyncKeyState(VK_F8) & 0x01)
	{
		return true;
	}
	return false;
}

int UWindow_Controller::GetMornitorWidth()
{
	return GetSystemMetrics(SM_CXSCREEN);
}

int UWindow_Controller::GetMornitorHeight()
{
	return GetSystemMetrics(SM_CYSCREEN);
}

