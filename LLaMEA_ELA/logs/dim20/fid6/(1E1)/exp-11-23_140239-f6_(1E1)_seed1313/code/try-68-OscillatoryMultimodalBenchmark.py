import numpy as np

class OscillatoryMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        result = 0.1 * np.sum(x**2)
        
        # Add periodic modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            # Use sine and cosine combinations to create complex oscillatory behavior
            freq = (i + 1) * 0.5
            amp = 2.0 / (i + 1)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Introduce multi-modal structure using Gaussian peaks with random positions
        num_peaks = min(5, self.dim)
        for i in range(num_peaks):
            # Random peak locations and heights
            peak_pos = np.random.uniform(-4.0, 4.0, self.dim)
            peak_height = np.random.uniform(1.0, 3.0)
            
            # Gaussian contribution from each peak
            gaussian = np.exp(-np.sum((x - peak_pos)**2) / (2 * 0.5**2))
            result += peak_height * gaussian
        
        # Add a sinusoidal spiral component for added complexity in higher dimensions
        if self.dim >= 2:
            spiral_term = np.sin(x[0] * x[1]) * np.cos(x[0] + x[1])
            result += 0.5 * spiral_term
        
        # Add noise to increase ruggedness
        noise = 0.05 * np.sum(np.random.uniform(-1, 1, self.dim))
        
        return result + noise