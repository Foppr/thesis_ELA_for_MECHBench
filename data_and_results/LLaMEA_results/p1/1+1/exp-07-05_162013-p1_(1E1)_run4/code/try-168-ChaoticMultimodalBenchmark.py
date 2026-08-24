import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute hyperchaotic constants with increased complexity
        self.r1 = 3.9
        self.r2 = 3.7
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate a hyperchaotic sequence using coupled logistic maps
        seq = np.zeros(self.dim)
        x1, x2 = 0.5, 0.3
        for i in range(self.dim):
            x1 = self.r1 * x1 * (1 - x1)
            x2 = self.r2 * x2 * (1 - x2)
            seq[i] = 0.5 * (x1 + x2) + 0.2 * np.sin(i * np.pi / self.dim) + 0.1 * np.cos(i * np.pi / (self.dim * 2))
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Hyperchaotic polynomial component with dynamic exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponents = [2, 3, 4, 5, 6, 7, 8]
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            result += chaotic_factor * (x[i]**exp - exp*x[i]**(exp-1) + (exp*(exp-1)/2)*x[i]**(exp-2) + (exp*(exp-1)*(exp-2)/6)*x[i]**(exp-3))
            
        # Hyperchaotic trigonometric coupling with dynamic frequencies and amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                amp = 0.4 * (1 + np.sin(4 * phase)) * (1 + np.cos(2 * phase))
                freq1 = 4 * (1 + np.cos(3 * phase))
                freq2 = 3 * (1 + np.sin(3 * phase))
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Dynamic spherical penalty with hyperchaotic center and variable radius
        center = np.array([self.chaotic_sequence[i] * 4.0 for i in range(self.dim)])
        radius = 1.5 + 1.0 * np.sin(self.chaotic_sequence[0] * 15) * np.cos(self.chaotic_sequence[1] * 10)
        result += 0.5 * np.sum(((x - center) / radius)**2)
        
        # Multi-frequency hyperchaotic oscillation with varying amplitudes
        for i in range(self.dim):
            freq = 20 + 15 * self.chaotic_sequence[i]
            amp = 0.2 + 0.1 * np.cos(7 * self.chaotic_sequence[i])
            result += amp * np.sin(freq * x[i])
            
        # Add global minimum attractor with hyperchaotic scaling
        scale = 0.08 + 0.04 * np.sin(self.chaotic_sequence[0] * 25)
        result += scale * np.sum(x**2)
        
        # Add hyperchaotic noise term
        noise = 0.02 * np.sum(np.sin(self.chaotic_sequence * x))
        result += noise
        
        # Add hyperchaotic modulation with increased complexity
        modulate = 0.05 * np.sum(np.cos(self.chaotic_sequence * x**2)) * (1 + 0.1 * np.sin(self.chaotic_sequence[0] * 30))
        result += modulate
        
        # Add hyperchaotic interaction term with higher frequency
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 10 * (1 + np.sin(self.chaotic_sequence[i] * 10))
                result += 0.06 * freq * np.sin(x[i] + x[j]) * np.cos(self.chaotic_sequence[i] * x[j])
        
        # Add hyperchaotic coupling term with multiple interaction modes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq1 = 6 * (1 + np.sin(self.chaotic_sequence[i] * 6))
                freq2 = 5 * (1 + np.cos(self.chaotic_sequence[j] * 5))
                result += 0.07 * freq1 * freq2 * np.sin(x[i] * x[j]) * np.sin(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
        
        # Add higher order polynomial chaos interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * (x[i]**4 + x[j]**4) * np.cos(self.chaotic_sequence[i] * x[j])
        
        # Add hyperchaotic sinusoidal coupling with variable phase shifts
        for i in range(self.dim):
            phase_shift = 0.7 * np.sin(self.chaotic_sequence[i] * 10)
            result += 0.04 * np.sin(5 * x[i] + phase_shift) * np.cos(4 * x[i] + phase_shift)
        
        # Add hyperchaotic interaction with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_factor = np.exp(-0.5 * (x[i] - x[j])**2)
                result += 0.05 * exp_factor * np.sin(self.chaotic_sequence[i] * x[j]) * np.cos(self.chaotic_sequence[j] * x[i])
        
        # Add a new hyperchaotic interaction with cubic terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * (x[i]**3 + x[j]**3) * np.sin(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
        
        # Add a new hyperchaotic coupling with inverse frequency modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 12 / (1 + np.abs(self.chaotic_sequence[i] - self.chaotic_sequence[j]))
                result += 0.03 * freq * np.cos(x[i] + x[j]) * np.sin(self.chaotic_sequence[i] * x[j])
        
        return result