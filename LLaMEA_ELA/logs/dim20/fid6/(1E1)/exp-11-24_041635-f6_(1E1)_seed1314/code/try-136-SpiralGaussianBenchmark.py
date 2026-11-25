import numpy as np

class SpiralGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Create spiral arrangement of Gaussian peaks
        num_peaks = max(1, self.dim // 2)
        for i in range(num_peaks):
            # Spiral positioning
            angle = i * np.pi / 4
            radius = 1.0 + i * 0.5
            
            # Peak center coordinates
            center_x = radius * np.cos(angle)
            center_y = radius * np.sin(angle)
            
            # Gaussian peak with exponential decay
            peak_value = np.exp(-i * 0.3)
            
            # Calculate distance from peak center
            dist = np.sqrt((x[0] - center_x)**2 + (x[1] - center_y)**2)
            
            # Add Gaussian contribution
            result += peak_value * np.exp(-dist**2 / 2.0)
            
            # Add additional dimensions if available
            if self.dim > 2:
                for j in range(2, min(self.dim, num_peaks * 2)):
                    dist = np.sqrt((x[j] - center_x)**2 + (x[j-1] - center_y)**2)
                    result += peak_value * np.exp(-dist**2 / 2.0) * np.sin(j * 0.5)
        
        # Add chaotic modulation with sine waves
        chaos_mod = 0.0
        for i in range(self.dim):
            chaos_mod += np.sin(x[i] * (i + 1)) * np.cos(x[i] * 0.3 * (i + 1))
            
        result += 0.5 * chaos_mod
        
        # Add polynomial terms for additional complexity
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += x[i]**4 * np.sin(x[i])
            
        result += 0.1 * poly_term
        
        return result