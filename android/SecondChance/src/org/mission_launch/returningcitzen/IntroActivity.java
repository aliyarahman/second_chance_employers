package org.mission_launch.returningcitzen;


import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.*;

public class IntroActivity extends Activity
{

	private Button infoButton;
	private Button rateButton;
	private Button supportButton;
	
	
	@Override
	protected void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_intro);
		
		infoButton = (Button) findViewById(R.id.infoButton);
		rateButton = (Button) findViewById(R.id.rateButton);
		supportButton = (Button) findViewById(R.id.supportButton);
		
		setupListeners();
	}
	
	private void setupListeners()
	{
		infoButton.setOnClickListener(new View.OnClickListener()
		{
			
			@Override
			public void onClick(View currentView)
			{
				Intent otherScreenIntent = new Intent(currentView.getContext(), InfoActivity.class);
				startActivityForResult(otherScreenIntent, 0);
				
			}
		});
		
		rateButton.setOnClickListener(new View.OnClickListener()
		{
			
			@Override
			public void onClick(View currentView)
			{
				Intent otherScreenIntent = new Intent(currentView.getContext(), RatingActivity.class);
				startActivityForResult(otherScreenIntent, 0);
				
			}
		});
		
		supportButton.setOnClickListener(new View.OnClickListener()
		{
			
			@Override
			public void onClick(View v)
			{
				// TODO Auto-generated method stub
				
			}
		});
	}
}
