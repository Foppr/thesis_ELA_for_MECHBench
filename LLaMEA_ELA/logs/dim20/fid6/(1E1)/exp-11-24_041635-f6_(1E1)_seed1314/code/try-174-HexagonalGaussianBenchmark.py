import numpy as np

class HexagonalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial sinusoidal component
        r = np.sqrt(np.sum(x**2))
        radial_sine = np.sin(2.0 * r) * np.exp(-0.15 * r)
        
        # Hexagonal Gaussian peaks
        peak_sum = 0.0
        num_peaks = min(25, self.dim * 3)
        
        # Generate hexagonal lattice points
        for i in range(num_peaks):
            # Hexagonal arrangement in 2D space
            angle = (i * np.pi / 3.0) % (2.0 * np.pi)
            radius = 1.0 + (i // 6) * 0.5
            
            peak_x = radius * np.cos(angle)
            peak_y = radius * np.sin(angle)
            
            # Adjust for dimensionality
            if self.dim >= 2:
                dx = x[0] - peak_x
                dy = x[1] - peak_y
                distance = np.sqrt(dx**2 + dy**2)
                
                # Gaussian peak with exponential decay
                peak_value = np.exp(-0.5 * (distance / (0.4 + i * 0.03))**2) * np.exp(-0.04 * i)
                peak_sum += peak_value
            
            # Add additional peaks in higher dimensions
            if self.dim > 2:
                for d in range(2, min(self.dim, num_peaks)):
                    if i < self.dim:
                        dx = x[d] - (i * 0.25)
                        peak_sum += np.exp(-0.5 * (dx / (0.2 + i * 0.01))**2) * np.exp(-0.02 * i)
        
        # Chaotic harmonic interference component
        chaotic = 0.0
        for i in range(self.dim):
            freq = 1.0 + i * 0.7
            amp = 1.0 / (1.0 + i * 0.3)
            # Add chaotic harmonic interference term to increase complexity
            harmonic = np.sin(freq * x[i]) * np.cos(freq * x[i] * 1.3) + \
                       0.4 * np.sin(2 * freq * x[i]) * np.cos(3 * freq * x[i])
            chaotic += amp * harmonic
        
        # Add a secondary chaotic modulation based on all dimensions
        modulate = np.sin(0.7 * r) * np.cos(0.4 * r) * np.sin(0.2 * r)
        
        # Combine all components
        result = radial_sine + peak_sum + chaotic + 0.15 * modulate
        
        return result