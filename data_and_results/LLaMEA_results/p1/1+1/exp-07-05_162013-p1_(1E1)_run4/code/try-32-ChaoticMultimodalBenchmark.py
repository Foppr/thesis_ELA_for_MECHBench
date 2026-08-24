import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants with enhanced complexity
        self.r = 3.8  # Slightly modified logistic map parameter for more chaos
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate a chaotic sequence using logistic map with enhanced sensitivity
        seq = np.zeros(self.dim)
        x = 0.5  # Initial value
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x
        # Add small perturbations for more complex dynamics
        seq += 0.01 * np.sin(np.arange(self.dim) * np.pi / self.dim)
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic polynomial component with higher-order terms
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            # Higher-order polynomial for increased nonlinearity
            result += chaotic_factor * (x[i]**5 - 5*x[i]**4 + 10*x[i]**3 - 10*x[i]**2 + 5*x[i] - 1)
            
        # Enhanced trigonometric coupling with multiple frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                # Multiple frequency components for increased complexity
                result += 0.3 * (np.sin(3 * np.pi * x[i] + phase) * np.cos(3 * np.pi * x[j] + phase) +
                                0.5 * np.sin(5 * np.pi * x[i] + phase) * np.cos(5 * np.pi * x[j] + phase))
                
        # Adaptive spherical penalty with chaotic center and dynamic radius
        center = np.array([self.chaotic_sequence[i] * 3.0 for i in range(self.dim)])
        radius = 1.0 + 0.5 * np.mean(self.chaotic_sequence)
        result += 0.4 * np.sum((x - center)**2) / (radius**2 + 1e-8)
        
        # Multi-frequency chaotic oscillation with varying amplitudes
        for i in range(self.dim):
            freq = 15 + 10 * self.chaotic_sequence[i]
            amp = 0.3 + 0.2 * np.sin(self.dim + i)
            result += amp * np.sin(freq * x[i] * self.chaotic_sequence[i])
            
        # Add global minimum attractor with chaotic scaling
        scale = 0.05 + 0.05 * np.mean(self.chaotic_sequence)
        result += scale * np.sum(x**2)
        
        # Add a small chaotic noise term to increase ruggedness
        noise = np.sum(np.sin(7 * x * self.chaotic_sequence) * self.chaotic_sequence)
        result += 0.05 * noise
        
        return result