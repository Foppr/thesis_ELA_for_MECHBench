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
        
        # Spiral Gaussian peaks with improved positioning and decay
        peak_sum = 0.0
        num_peaks = min(25, self.dim * 3)
        
        for i in range(num_peaks):
            # Position peaks in spiral pattern with better distribution
            angle = i * 0.6 + np.sin(i * 0.3) * 0.5
            radius = 1.0 + i * 0.25 + np.cos(i * 0.4) * 0.3
            peak_x = radius * np.cos(angle)
            peak_y = radius * np.sin(angle)
            
            # Adjust for dimensionality
            if self.dim >= 2:
                # Use first two dimensions for spiral placement
                dx = x[0] - peak_x
                dy = x[1] - peak_y
                distance = np.sqrt(dx**2 + dy**2)
                
                # Gaussian peak with improved exponential decay and width
                peak_value = np.exp(-0.5 * (distance / (0.4 + i * 0.03))**2) * np.exp(-0.04 * i)
                peak_sum += peak_value
            
            # Add additional peaks in higher dimensions with better spacing
            if self.dim > 2:
                for d in range(2, min(self.dim, num_peaks)):
                    if i < self.dim:
                        dx = x[d] - (i * 0.25 + np.sin(i * 0.5) * 0.1)
                        peak_sum += np.exp(-0.5 * (dx / (0.25 + i * 0.015))**2) * np.exp(-0.025 * i)
        
        # Enhanced multimodal component with improved harmonic interference
        multimodal = 0.0
        for i in range(self.dim):
            freq = 1.0 + i * 0.6 + np.sin(i * 0.7) * 0.3
            amp = 1.0 / (1.0 + i * 0.25 + np.cos(i * 0.5) * 0.1)
            # Add more complex harmonic interference term to increase complexity
            harmonic = np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) + 0.4 * np.sin(2 * freq * x[i]) + 0.2 * np.cos(3 * freq * x[i])
            multimodal += amp * harmonic
        
        # Add a secondary sinusoidal modulation based on all dimensions with improved structure
        modulate = np.sin(0.6 * r) * np.cos(0.4 * r) + 0.3 * np.sin(1.2 * r)
        
        # Combine all components with adjusted weights for better balance
        result = radial_sine + peak_sum + multimodal + 0.25 * modulate
        
        return result