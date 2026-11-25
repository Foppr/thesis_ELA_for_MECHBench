import numpy as np

class ChaoticCompositeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.alpha = 3.8
        self.beta = 0.5
        self.gamma = 2.0
        self.delta = 1.2
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component with logistic map influence
        chaotic_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Logistic map-like term with sinusoidal modulation
            chaotic_term = self.alpha * xi * (1 - xi) * np.sin(self.gamma * xi)
            chaotic_sum += chaotic_term ** 2
            
        # Radial symmetry component with multiple harmonic terms
        radius = np.linalg.norm(x)
        if radius == 0:
            radial_sum = 0
        else:
            radial_sum = (radius - self.beta) ** 2 * (
                1 + 0.3 * np.sin(radius) + 
                0.2 * np.cos(2 * radius) + 
                0.1 * np.sin(3 * radius)
            )
            
        # Cross-dimensional coupling with varying interaction strengths
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Distance-based coupling with exponential decay
                dist = np.abs(x[i] - x[j])
                coupling = np.sin(self.delta * dist) * np.exp(-0.1 * dist)
                coupling_sum += coupling ** 2
                
        # Sinusoidal modulation component
        sin_sum = 0
        for i in range(self.dim):
            # Multi-frequency sinusoidal terms with varying amplitudes
            freq1 = 1.0 + 0.5 * np.sin(i)
            freq2 = 2.0 + 0.3 * np.cos(i)
            freq3 = 0.5 + 0.2 * np.sin(i * 0.7)
            
            sin_sum += (
                0.5 * np.sin(freq1 * x[i]) ** 2 +
                0.3 * np.cos(freq2 * x[i]) ** 2 +
                0.2 * np.sin(freq3 * x[i]) ** 2
            )
            
        # Dimensionality-dependent scaling factor
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combine all components
        result = scale_factor * (chaotic_sum + radial_sum + coupling_sum + sin_sum)
        
        # Add small random noise for robustness
        noise = 0.01 * np.random.normal(0, 1)
        
        return result + noise + 0.5 * self.dim