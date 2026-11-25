import numpy as np

class ChaoticCompositeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with improved values for better discrimination
        self.alpha = 4.0
        self.beta = 0.7
        self.gamma = 2.5
        self.delta = 1.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with logistic map influence and additional nonlinearity
        chaotic_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced chaotic term with cubic nonlinearity and multiple sinusoidal modulations
            chaotic_term = self.alpha * xi * (1 - xi**2) * np.sin(self.gamma * xi) * np.cos(0.5 * xi)
            chaotic_sum += chaotic_term ** 2
            
        # Modified radial symmetry component with higher-order harmonic terms and conditioning
        radius = np.linalg.norm(x)
        if radius == 0:
            radial_sum = 0
        else:
            radial_sum = (radius - self.beta) ** 3 * (
                1 + 0.4 * np.sin(radius) + 
                0.3 * np.cos(2 * radius) + 
                0.2 * np.sin(3 * radius) +
                0.1 * np.cos(4 * radius)
            )
            
        # Strengthened cross-dimensional coupling with adaptive interaction strengths
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Distance-based coupling with inverse quadratic decay and amplitude modulation
                dist = np.abs(x[i] - x[j])
                amp_mod = 1.0 + 0.2 * np.sin(0.3 * (i + j))
                coupling = amp_mod * np.sin(self.delta * dist) / (1 + 0.1 * dist**2)
                coupling_sum += coupling ** 2
                
        # Enhanced sinusoidal modulation component with frequency-dependent amplitudes
        sin_sum = 0
        for i in range(self.dim):
            # Multi-frequency sinusoidal terms with varying amplitudes and phase shifts
            freq1 = 1.5 + 0.3 * np.sin(i * 0.5)
            freq2 = 2.5 + 0.2 * np.cos(i * 0.7)
            freq3 = 0.8 + 0.1 * np.sin(i * 0.9)
            
            sin_sum += (
                0.6 * np.sin(freq1 * x[i]) ** 2 +
                0.4 * np.cos(freq2 * x[i]) ** 2 +
                0.3 * np.sin(freq3 * x[i]) ** 2
            )
            
        # Dimensionality-dependent scaling factor with improved conditioning
        scale_factor = 1.0 + 0.15 * np.log(self.dim + 1)
        
        # Combine all components with adjusted weights for better balance
        result = scale_factor * (0.7 * chaotic_sum + 0.8 * radial_sum + 0.6 * coupling_sum + sin_sum)
        
        # Add small random noise for robustness
        noise = 0.005 * np.random.normal(0, 1)
        
        return result + noise + 0.3 * self.dim