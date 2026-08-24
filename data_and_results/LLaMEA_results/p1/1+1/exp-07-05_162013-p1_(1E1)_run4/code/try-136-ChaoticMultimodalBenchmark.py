import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic constants with higher complexity
        self.r = 3.95  # Increased chaos parameter
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate highly complex chaotic sequence using multiple map iterations
        seq = np.zeros(self.dim)
        x = 0.5
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            x = 3.8 * x * (1 - x)  # Double logistic map for more complexity
            seq[i] = x + 0.15 * np.sin(i * np.pi / self.dim) + 0.05 * np.cos(i * np.pi / (self.dim * 2))  # Multi-frequency modulation
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Hyperchaotic polynomial component with higher exponents and variable coefficients
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponents = [2, 3, 4, 5, 6, 7, 8]
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            # Use higher order polynomial with chaotic coefficients
            coeff = 0.5 + 0.5 * np.sin(chaotic_factor * 10)
            result += coeff * (x[i]**exp - exp*x[i]**(exp-1) + (exp*(exp-1)/2)*x[i]**(exp-2) + (exp*(exp-1)*(exp-2)/6)*x[i]**(exp-3))
            
        # Hyperchaotic trigonometric coupling with multiple frequencies and chaotic amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                amp = 0.4 * (1 + np.sin(4 * phase)) * (1 + np.cos(3 * phase))  # Multi-frequency amplitude modulation
                freq1 = 4 * (1 + np.cos(3 * phase))
                freq2 = 3 * (1 + np.sin(3 * phase))
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Hyperchaotic spherical penalty with multi-scale chaotic center and variable radius
        center = np.array([self.chaotic_sequence[i] * 4.0 for i in range(self.dim)])
        radius = 1.5 + 1.0 * np.sin(self.chaotic_sequence[0] * 15) * np.cos(self.chaotic_sequence[1] * 10)  # Multi-scale radius
        result += 0.5 * np.sum(((x - center) / radius)**2)
        
        # Multi-frequency hyperchaotic oscillation with varying amplitudes and phases
        for i in range(self.dim):
            freq = 20 + 15 * self.chaotic_sequence[i]
            amp = 0.2 + 0.1 * np.cos(6 * self.chaotic_sequence[i])
            phase = 0.3 * np.sin(self.chaotic_sequence[i] * 12)
            result += amp * np.sin(freq * x[i] + phase)
            
        # Add global minimum attractor with hyperchaotic scaling
        scale = 0.08 + 0.04 * np.sin(self.chaotic_sequence[0] * 25)
        result += scale * np.sum(x**2)
        
        # Add a complex chaotic noise term to increase landscape complexity
        noise = 0.02 * np.sum(np.sin(self.chaotic_sequence * x) * np.cos(self.chaotic_sequence * x**2))
        result += noise
        
        # Add a new hyperchaotic modulation term
        modulate = 0.05 * np.sum(np.cos(self.chaotic_sequence * x**2) * np.sin(self.chaotic_sequence * x))
        result += modulate
        
        # Add a new hyperchaotic interaction term with different frequency and amplitude
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 10 * (1 + np.sin(self.chaotic_sequence[i] * 10)) * (1 + np.cos(self.chaotic_sequence[j] * 8))
                amp = 0.08 * (1 + np.cos(self.chaotic_sequence[i] * 12))
                result += amp * freq * np.sin(x[i] + x[j]) * np.cos(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
        
        # Add a new hyperchaotic coupling term with higher order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 8 * (1 + np.cos(self.chaotic_sequence[i] * 6)) * (1 + np.sin(self.chaotic_sequence[j] * 5))
                result += 0.06 * freq * np.sin(x[i] * x[j]) * np.sin(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
        
        # Add a new polynomial hyperchaos interaction with higher order terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * (x[i]**4 + x[j]**4) * np.cos(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
        
        # Add a new chaotic sinusoidal coupling with variable phase shifts and multi-frequency components
        for i in range(self.dim):
            phase_shift = 0.6 * np.sin(self.chaotic_sequence[i] * 10) + 0.4 * np.cos(self.chaotic_sequence[i] * 15)
            result += 0.04 * np.sin(5 * x[i] + phase_shift) * np.cos(4 * x[i] + phase_shift)
        
        # Add a new hyperchaotic interaction term with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_factor = np.exp(-self.chaotic_sequence[i] * 0.5)
                result += 0.07 * exp_factor * np.sin(x[i] + x[j]) * np.cos(x[i] * x[j])
        
        return result