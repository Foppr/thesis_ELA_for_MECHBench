import numpy as np

class HexagonalCubicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial sinusoidal component
        r = np.sqrt(np.sum(x**2))
        radial_sine = np.sin(2.0 * r) * np.exp(-0.1 * r)
        
        # Hexagonal grid of cubic peaks
        peak_sum = 0.0
        num_peaks = min(15, self.dim * 2)
        
        # Generate hexagonal grid points
        for i in range(num_peaks):
            # Hexagonal arrangement
            angle = i * np.pi / 3.0
            radius = 0.5 + i * 0.2
            
            peak_x = radius * np.cos(angle)
            peak_y = radius * np.sin(angle)
            
            if self.dim >= 2:
                dx = x[0] - peak_x
                dy = x[1] - peak_y
                distance = np.sqrt(dx**2 + dy**2)
                
                # Cubic peak with varying height and width
                peak_height = 1.0 / (1.0 + i * 0.1)
                peak_width = 0.3 + i * 0.05
                cubic_peak = peak_height * (1.0 - (distance / peak_width)**3)**3
                cubic_peak = np.maximum(cubic_peak, 0.0)
                peak_sum += cubic_peak
            
            # Add additional peaks in higher dimensions
            if self.dim > 2:
                for d in range(2, min(self.dim, num_peaks)):
                    if i < self.dim:
                        dx = x[d] - (i * 0.2)
                        width = 0.4 + i * 0.03
                        cubic_peak = (1.0 - np.abs(dx / width)**3)**3
                        cubic_peak = np.maximum(cubic_peak, 0.0)
                        peak_sum += cubic_peak
        
        # Additional quadratic component with varying conditioning
        quad_component = 0.0
        for i in range(self.dim):
            freq = 1.0 + i * 0.3
            amp = 1.0 / (1.0 + i * 0.1)
            quad_component += amp * (x[i] - i * 0.1)**2 * np.sin(freq * x[i])
        
        # Combine all components
        result = radial_sine + peak_sum + quad_component
        
        return result