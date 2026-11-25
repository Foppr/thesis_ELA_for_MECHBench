import numpy as np

class HelicalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Helical spiral component
        r = np.sqrt(np.sum(x**2))
        helix = np.sin(5.0 * r) * np.cos(3.0 * r) * np.exp(-0.1 * r)
        
        # Helical Gaussian peaks in spiral pattern
        peak_sum = 0.0
        num_peaks = min(30, self.dim * 3)
        
        for i in range(num_peaks):
            # Position peaks in helical spiral pattern
            angle = i * 0.3
            radius = 1.0 + i * 0.2
            height = i * 0.1
            
            if self.dim >= 2:
                peak_x = radius * np.cos(angle)
                peak_y = radius * np.sin(angle)
                
                dx = x[0] - peak_x
                dy = x[1] - peak_y
                distance = np.sqrt(dx**2 + dy**2)
                
                # Gaussian peak with exponential decay and varying width
                sigma = 0.3 + i * 0.02
                peak_value = np.exp(-0.5 * (distance / sigma)**2) * np.exp(-0.03 * i)
                peak_sum += peak_value
            
            # Add higher dimensional peaks with varying influence
            if self.dim > 2:
                for d in range(2, min(self.dim, num_peaks)):
                    if i < self.dim:
                        dx = x[d] - (i * 0.2 + height)
                        sigma = 0.2 + i * 0.01
                        peak_sum += np.exp(-0.5 * (dx / sigma)**2) * np.exp(-0.02 * i)
        
        # Polynomial chaos component with adaptive conditioning
        poly_chaos = 0.0
        for i in range(self.dim):
            # Varying polynomial orders and coefficients
            order = 2 + i % 4
            coeff = 1.0 / (1.0 + i * 0.1)
            
            # Add chaotic interaction terms between dimensions
            interaction = 0.0
            for j in range(min(3, self.dim)):
                if i != j:
                    interaction += x[i] * x[j] * np.sin(i * j * 0.5)
            
            poly_chaos += coeff * (x[i]**order) + 0.1 * interaction
        
        # Adaptive conditioning component
        cond_factor = 0.0
        for i in range(self.dim):
            cond_factor += (i + 1) * np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 2))
        
        # Combine all components with varying weights
        result = helix + peak_sum + 0.5 * poly_chaos + 0.3 * cond_factor
        
        return result