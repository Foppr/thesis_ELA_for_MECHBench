import numpy as np

class SpiralGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial sinusoidal component
        r = np.sqrt(np.sum(x**2))
        radial_sine = np.sin(3.0 * r) * np.exp(-0.1 * r)
        
        # Spiral Gaussian peaks
        peak_sum = 0.0
        num_peaks = min(20, self.dim * 2)
        
        for i in range(num_peaks):
            # Position peaks in spiral pattern
            angle = i * 0.5
            radius = 1.0 + i * 0.3
            peak_x = radius * np.cos(angle)
            peak_y = radius * np.sin(angle)
            
            # Adjust for dimensionality
            if self.dim >= 2:
                # Use first two dimensions for spiral placement
                dx = x[0] - peak_x
                dy = x[1] - peak_y
                distance = np.sqrt(dx**2 + dy**2)
                
                # Gaussian peak with exponential decay
                peak_value = np.exp(-0.5 * (distance / (0.5 + i * 0.05))**2) * np.exp(-0.05 * i)
                peak_sum += peak_value
            
            # Add additional peaks in higher dimensions
            if self.dim > 2:
                for d in range(2, min(self.dim, num_peaks)):
                    if i < self.dim:
                        dx = x[d] - (i * 0.3)
                        peak_sum += np.exp(-0.5 * (dx / (0.3 + i * 0.02))**2) * np.exp(-0.03 * i)
        
        # Additional multimodal component with varying amplitudes
        multimodal = 0.0
        for i in range(self.dim):
            freq = 1.0 + i * 0.5
            amp = 1.0 / (1.0 + i * 0.2)
            multimodal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Combine all components
        result = radial_sine + peak_sum + multimodal
        
        return result