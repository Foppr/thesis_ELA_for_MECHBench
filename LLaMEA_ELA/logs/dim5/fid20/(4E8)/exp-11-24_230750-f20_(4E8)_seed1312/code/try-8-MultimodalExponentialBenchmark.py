import numpy as np

class MultimodalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 2.0)
        
        # Multiple exponential peaks arranged in a circular pattern
        peak_term = 0.0
        num_peaks = 8
        for i in range(num_peaks):
            angle = 2 * np.pi * i / num_peaks
            peak_x = 3.0 * np.cos(angle)
            peak_y = 3.0 * np.sin(angle)
            dist = np.sqrt((x[0] - peak_x)**2 + (x[1] - peak_y)**2)
            peak_term += np.exp(-dist**2 / 0.5)
        
        # Polynomial penalty terms to create varied conditioning
        poly_term = 0.1 * np.sum(x**4) + 0.05 * np.sum(x**3)
        
        # Cross-terms for increased complexity
        cross_term = 0.02 * np.sum(x[:-1] * x[1:])
        
        # Combine all terms
        result = -radial_term + peak_term + poly_term + cross_term
        
        # Shift to ensure global minimum is at origin and function is bounded below
        return result + 5.0