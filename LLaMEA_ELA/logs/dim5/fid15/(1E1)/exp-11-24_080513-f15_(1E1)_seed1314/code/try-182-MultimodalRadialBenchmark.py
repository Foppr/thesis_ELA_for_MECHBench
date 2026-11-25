import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial Gaussian peaks with varying heights and widths
        peak_values = []
        for i in range(12):  # 12 peaks
            # Peak center
            center = np.sin(i * 0.5) * 0.8, np.cos(i * 0.5) * 0.8
            # Peak height and width
            height = 1.0 + 0.5 * np.sin(i * 0.3)
            width = 0.2 + 0.3 * np.cos(i * 0.4)
            
            # Distance from center
            dist_sq = (x_normalized[0] - center[0])**2 + (x_normalized[1] - center[1])**2
            
            # Gaussian peak
            peak_val = height * np.exp(-dist_sq / (2 * width**2))
            peak_values.append(peak_val)
        
        # Sum of peaks
        radial_term = sum(peak_values)
        
        # Sinusoidal modulation to create complex valleys
        sin_mod = 0.0
        for i in range(self.dim):
            sin_mod += np.sin(x_normalized[i] * 5.0) * np.cos(x_normalized[i] * 3.0)
            
        # Add a global quadratic term to bias towards origin
        quadratic = 0.1 * np.sum(x_normalized**2)
        
        # Combine all components
        return radial_term + 0.5 * sin_mod + quadratic