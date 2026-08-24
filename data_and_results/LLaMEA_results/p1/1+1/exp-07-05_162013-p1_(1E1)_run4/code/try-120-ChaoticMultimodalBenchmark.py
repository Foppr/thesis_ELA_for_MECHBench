import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute highly complex chaotic constants with fractal-like properties
        self.r = 3.99  # Increased chaos parameter
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate a fractal-like chaotic sequence using multiple chaotic maps
        seq = np.zeros(self.dim)
        x1, x2 = 0.5, 0.3  # Dual initial values for higher complexity
        for i in range(self.dim):
            x1 = self.r * x1 * (1 - x1)
            x2 = self.r * x2 * (1 - x2)
            seq[i] = (x1 + x2) / 2 + 0.05 * np.sin(i * np.pi / self.dim) + 0.03 * np.cos(i * np.pi / (self.dim * 2))
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Hyperchaotic polynomial component with nested exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            # Use nested variable exponents based on chaotic sequence
            exponents = [2, 3, 4, 5, 6, 7, 8]
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            # Add nested polynomial terms for higher complexity
            result += chaotic_factor * (x[i]**exp + 0.5 * x[i]**(exp-1) + 0.2 * x[i]**(exp-2) + 0.1 * x[i]**(exp-3))
            
        # Hyperchaotic trigonometric coupling with nested frequencies and dynamic amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j] + 0.1 * np.sin(x[i] + x[j])
                amp = 0.4 * (1 + np.sin(4 * phase)) * (1 + np.cos(2 * phase))  # Dynamic amplitude
                freq1 = 5 * (1 + np.cos(3 * phase)) * (1 + np.sin(2 * phase))
                freq2 = 4 * (1 + np.sin(3 * phase)) * (1 + np.cos(2 * phase))
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Dynamic spherical penalty with hyperchaotic center and variable radius
        center = np.array([self.chaotic_sequence[i] * 4.0 for i in range(self.dim)])
        radius = 1.5 + 1.0 * np.sin(self.chaotic_sequence[0] * 15) * np.cos(self.chaotic_sequence[1] * 10)
        result += 0.5 * np.sum(((x - center) / radius)**2)
        
        # Multi-frequency hyperchaotic oscillation with variable amplitudes and phases
        for i in range(self.dim):
            freq = 20 + 15 * self.chaotic_sequence[i] + 5 * np.sin(self.chaotic_sequence[i] * 12)
            amp = 0.2 + 0.1 * np.cos(7 * self.chaotic_sequence[i]) * np.sin(3 * self.chaotic_sequence[i])
            phase = 0.3 * np.sin(self.chaotic_sequence[i] * 8)
            result += amp * np.sin(freq * x[i] + phase)
            
        # Add global minimum attractor with hyperchaotic scaling
        scale = 0.08 + 0.04 * np.sin(self.chaotic_sequence[0] * 25) * np.cos(self.chaotic_sequence[1] * 15)
        result += scale * np.sum(x**2)
        
        # Add a complex chaotic noise term to increase landscape complexity
        noise = 0.02 * np.sum(np.sin(self.chaotic_sequence * x) * np.cos(x**2))
        result += noise
        
        # Add a new hyperchaotic modulation to improve fitness score
        modulate = 0.05 * np.sum(np.cos(self.chaotic_sequence * x**3))  # Increased coefficient and cubic modulation
        result += modulate
        
        # Add a new hyperchaotic interaction term with nested frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 10 * (1 + np.sin(self.chaotic_sequence[i] * 10)) * (1 + np.cos(self.chaotic_sequence[j] * 8))
                result += 0.06 * freq * np.sin(x[i] + x[j]) * np.cos(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
        
        # Add a new hyperchaotic coupling term with nested phases
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 8 * (1 + np.cos(self.chaotic_sequence[i] * 6)) * (1 + np.sin(self.chaotic_sequence[j] * 5))
                phase = 0.2 * np.sin(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
                result += 0.07 * freq * np.sin(x[i] * x[j] + phase) * np.sin(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
        
        # Add a new polynomial hyperchaos interaction with higher order terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * (x[i]**4 + x[j]**4) * np.cos(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
        
        # Add a new hyperchaotic sinusoidal coupling with variable phase shifts
        for i in range(self.dim):
            phase_shift = 0.7 * np.sin(self.chaotic_sequence[i] * 10) + 0.3 * np.cos(self.chaotic_sequence[i] * 5)
            result += 0.04 * np.sin(5 * x[i] + phase_shift) * np.cos(4 * x[i] + phase_shift)
        
        # Add a new fractal-like interaction term
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 12 * (1 + np.sin(self.chaotic_sequence[i] * 12) * np.cos(self.chaotic_sequence[j] * 10))
                result += 0.08 * freq * np.sin(x[i]**2 + x[j]**2) * np.cos(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
        
        return result