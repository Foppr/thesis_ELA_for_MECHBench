import numpy as np

class SpiralGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial sinusoidal component with higher frequency
        r = np.sqrt(np.sum(x**2))
        radial_sine = np.sin(5.0 * r) * np.exp(-0.15 * r)
        
        # Spiral Gaussian peaks with increased complexity
        peak_sum = 0.0
        num_peaks = min(30, self.dim * 3)
        
        for i in range(num_peaks):
            # Position peaks in spiral pattern with more complex arrangement
            angle = i * 0.7 + np.sin(i * 0.3) * 0.5
            radius = 1.2 + i * 0.4 + np.cos(i * 0.2) * 0.3
            peak_x = radius * np.cos(angle)
            peak_y = radius * np.sin(angle)
            
            # Adjust for dimensionality
            if self.dim >= 2:
                # Use first two dimensions for spiral placement
                dx = x[0] - peak_x
                dy = x[1] - peak_y
                distance = np.sqrt(dx**2 + dy**2)
                
                # Gaussian peak with stronger exponential decay and variable width
                peak_value = np.exp(-0.5 * (distance / (0.3 + i * 0.03))**2) * np.exp(-0.1 * i)
                peak_sum += peak_value
            
            # Add additional peaks in higher dimensions with more complex positioning
            if self.dim > 2:
                for d in range(2, min(self.dim, num_peaks)):
                    if i < self.dim:
                        # More complex peak placement using trigonometric functions
                        dx = x[d] - (i * 0.4 + np.sin(i * 0.5) * 0.2)
                        peak_sum += np.exp(-0.5 * (dx / (0.2 + i * 0.01))**2) * np.exp(-0.08 * i)
        
        # Additional multimodal component with high-frequency oscillations
        multimodal = 0.0
        for i in range(self.dim):
            freq = 2.0 + i * 0.8 + np.sin(i * 0.3) * 0.5
            amp = 1.5 / (1.0 + i * 0.3 + np.cos(i * 0.4) * 0.2)
            multimodal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8) * np.exp(-0.05 * i)
        
        # Add a new component with hyperbolic tangent modulation for additional complexity
        tanh_component = 0.0
        for i in range(self.dim):
            tanh_component += np.tanh(x[i] * (1.0 + i * 0.1)) * np.sin(i * 0.5) * np.cos(i * 0.3)
        
        # Combine all components with different weights
        result = radial_sine + peak_sum + multimodal + 0.5 * tanh_component
        
        return result