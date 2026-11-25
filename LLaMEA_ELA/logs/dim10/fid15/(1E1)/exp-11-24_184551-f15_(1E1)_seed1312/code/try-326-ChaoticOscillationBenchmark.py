import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Normalize input to [-1, 1] for chaotic behavior
        x_norm = x / 5.0
        
        # Radial basin term - pulls towards origin
        radial_term = np.sum(x_norm**2) * 0.5
        
        # Chaotic oscillation terms using sine and cosine with different frequencies
        oscillation_term = 0.0
        for i in range(self.dim):
            # Use different frequencies for each dimension
            freq = i + 1
            oscillation_term += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
            
        # Cross-terms creating non-separability
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x_norm[i] * x_norm[j] * np.sin(x_norm[i] + x_norm[j])
                
        # Add a chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(10 * np.pi * x_norm[i]) * np.cos(5 * np.pi * x_norm[i])
            
        # Combine all terms with different weights
        result = radial_term - 0.5 * oscillation_term + 0.3 * cross_term - 0.2 * chaotic_term
        
        # Add small noise for realism
        noise = np.sum(np.random.normal(0, 0.01, self.dim))
        
        return result + noise