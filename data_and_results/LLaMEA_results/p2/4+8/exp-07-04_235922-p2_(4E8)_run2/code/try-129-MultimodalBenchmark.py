import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add chaotic polynomial terms with sinusoidal modulation
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**7 - 21*xi**5 + 175*xi**3 - 315*xi
            trig_term = np.sin(3 * xi) * np.cos(2 * xi) + 0.3 * np.sin(7 * xi) * np.cos(5 * xi)
            result += 0.15 * poly_term * trig_term
        
        # Add chaotic coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.3 * x[i]) * np.cos(0.4 * x[j]) + np.cos(0.5 * x[i]) * np.sin(0.6 * x[j])
                result += 0.25 * coupling * (x[i]**2 + x[j]**2 + 1.0)
        
        # Add chaotic radial barriers with dynamic scaling
        radial_sum = 0.0
        for i in range(self.dim):
            radial_sum += (x[i] - 2.0)**2 + (x[i] + 2.0)**2
        barrier = 0.6 * np.exp(-0.15 * radial_sum) + 0.4 * np.exp(-0.08 * radial_sum**2) + 0.2 * np.sin(0.5 * radial_sum)
        result += barrier
        
        # Add chaotic conditioning based on dimensionality
        conditioning = 1.0 + 0.12 * np.sin(self.dim * 0.8) * np.cos(self.dim * 0.5) + 0.08 * np.sin(self.dim * 1.1)
        result *= conditioning
        
        # Add multi-scale chaotic modulation
        modulate = 0.0
        for i in range(self.dim):
            modulate += np.sin(5 * x[i]) * np.cos(4 * x[i]) * np.exp(-0.03 * x[i]**2) + 0.25 * np.sin(8 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.02 * x[i]**2)
        result += 0.25 * modulate
        
        # Add chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(10 * x[i]) * np.cos(9 * x[i]) * np.exp(-0.04 * x[i]**2) + 0.15 * np.sin(13 * x[i]) * np.cos(12 * x[i])
        result += 0.02 * noise
        
        # Add chaotic non-smooth elements
        smooth_term = 0.0
        for i in range(self.dim):
            smooth_term += np.abs(x[i])**1.5 + 0.5 * np.abs(x[i])**2.5
        result += 0.1 * smooth_term
        
        return result