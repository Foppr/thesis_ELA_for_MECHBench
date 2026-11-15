import numpy as np

class LabyrinthineHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with conditioning
        f = 0.5 * np.sum(x**2)
        
        # Add labyrinthine harmonic waves with exponential decay
        for i in range(self.dim):
            f += 2.0 * np.exp(-0.1 * i) * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            
        # Add directional bias fields with varying strength
        bias_strength = 0.5
        for i in range(self.dim):
            f += bias_strength * (x[i] - 2.0)**2 * np.sin(0.5 * np.pi * x[i])
            
        # Add multi-scale oscillatory patterns with frequency modulation
        for i in range(self.dim):
            freq = 2**(i % 4)  # Varying frequencies
            f += 0.8 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.sin(freq * x[i] * 0.3)
            
        # Add adaptive noise with amplitude dependent on position
        noise_amp = 0.1 + 0.05 * np.abs(x).mean()
        f += noise_amp * np.sum(np.sin(10 * x + np.random.rand(self.dim) * np.pi))
        
        # Add coupled harmonic interactions with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = np.exp(-0.05 * (i + j))
                f += coupling * np.sin(2 * x[i] + x[j]) * np.cos(3 * x[i] - x[j])
                
        # Add fractal-like self-similarity with recursive pattern
        for i in range(self.dim):
            f += 0.3 * np.sin(5 * np.sin(2 * x[i])) * np.cos(4 * np.cos(3 * x[i]))
            
        # Add asymmetric harmonic terms to increase complexity
        for i in range(self.dim):
            f += 0.2 * np.sin(4 * x[i]) * np.cos(2 * x[i]) * np.sin(0.5 * x[i]) * np.cos(0.25 * x[i])
            
        # Add exponential decay terms with global minima at non-zero locations
        global_minima = np.array([1.0, -1.0, 2.0, -2.0, 3.0, -3.0])
        minima_term = 0
        for i in range(min(len(global_minima), self.dim)):
            minima_term += np.exp(-0.5 * (x[i] - global_minima[i])**2)
        f += 0.4 * minima_term
        
        # Add directional dependency with cosine modulation
        direction_term = 0
        for i in range(self.dim):
            direction_term += np.cos(0.1 * x[i]) * np.sin(0.2 * x[i])
        f += 0.3 * direction_term
        
        # Add higher-order polynomial with harmonic modulation
        for i in range(self.dim):
            f += 0.1 * x[i]**3 * np.sin(2 * x[i])
            
        return f