import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency patterns for fractal-like behavior
        self.freq_patterns = np.array([2**i for i in range(10)])
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Fractal-like component with self-similar structure
        fractal = 0.0
        for i in range(self.dim):
            freq = self.freq_patterns[i % len(self.freq_patterns)]
            fractal += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Dynamic dimensional coupling with time-varying interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-varying interaction strength
                t = 0.5 + 0.5 * np.sin(0.1 * (i + j))
                coupling += t * np.sin(20 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(15 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Multi-scale sinusoidal landscape with varying amplitudes
        multiscale = 0.0
        for i in range(self.dim):
            scale = 1 + 0.5 * np.sin(0.3 * i)
            multiscale += scale * np.sin(30 * np.pi * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Chaotic component with logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            # Logistic-like chaotic behavior
            chaotic += 0.4 * np.sin(60 * np.pi * x_norm[i]) * np.cos(50 * np.pi * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
        
        # Adaptive penalty with dynamic threshold
        penalty = 0.0
        for i in range(self.dim):
            # Dynamic threshold based on dimension
            threshold = 1.0 + 0.2 * np.sin(0.2 * i)
            penalty += 0.3 * (np.abs(x_norm[i]) - threshold)**2 * np.exp(-0.1 * x_norm[i]**2)
        
        # Cross-dimensional exponential interaction
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += 0.25 * np.exp(-2.0 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(25 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Time-varying global structure
        global_structure = 0.0
        for i in range(self.dim):
            # Time-varying phase
            phase = np.sin(0.1 * i)
            global_structure += 0.15 * np.sin(35 * np.pi * x_norm[i] + phase) * np.cos(30 * np.pi * x_norm[i] + phase)
        
        # Add all components together
        total = quadratic + fractal + coupling + multiscale + chaotic + penalty + cross_exp + global_structure
        
        # Add a small noise term to increase robustness challenge
        noise = 0.01 * np.random.rand()
        
        return total + noise