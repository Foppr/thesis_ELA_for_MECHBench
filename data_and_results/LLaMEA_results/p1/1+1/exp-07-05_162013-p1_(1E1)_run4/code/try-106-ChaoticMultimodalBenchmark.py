import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants with enhanced complexity
        self.r = 3.9  # Slightly different logistic map parameter for more chaos
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate a more complex chaotic sequence using logistic map with offset
        seq = np.zeros(self.dim)
        x = 0.5  # Initial value
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x + 0.15 * np.sin(i * np.pi / self.dim)  # Add sinusoidal modulation
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced chaotic polynomial component with variable exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            # Use variable exponents based on chaotic sequence
            exponents = [2, 3, 4, 5, 6, 7]
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            result += chaotic_factor * (x[i]**exp - exp*x[i]**(exp-1) + (exp*(exp-1)/2)*x[i]**(exp-2))
            
        # Enhanced trigonometric coupling with multiple frequencies and chaotic amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                amp = 0.4 * (1 + np.sin(4 * phase))  # Adaptive amplitude
                freq1 = 4 * (1 + np.cos(3 * phase))
                freq2 = 3 * (1 + np.sin(3 * phase))
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Adaptive spherical penalty with chaotic center and variable radius
        center = np.array([self.chaotic_sequence[i] * 2.5 for i in range(self.dim)])
        radius = 2.0 + 0.3 * np.sin(self.chaotic_sequence[0] * 12)
        result += 0.5 * np.sum(((x - center) / radius)**2)
        
        # Multi-frequency chaotic oscillation with varying amplitudes
        for i in range(self.dim):
            freq = 18 + 8 * self.chaotic_sequence[i]
            amp = 0.2 + 0.03 * np.cos(6 * self.chaotic_sequence[i])
            result += amp * np.sin(freq * x[i])
            
        # Add global minimum attractor with chaotic scaling
        scale = 0.06 + 0.04 * np.sin(self.chaotic_sequence[0] * 25)
        result += scale * np.sum(x**2)
        
        # Add a small chaotic noise term to increase landscape complexity
        noise = 0.015 * np.sum(np.sin(self.chaotic_sequence * x))
        result += noise
        
        # Add a new chaotic modulation to improve fitness score - slightly modified coefficients
        modulate = 0.04 * np.sum(np.cos(self.chaotic_sequence * x**2))  # Increased coefficient
        result += modulate
        
        # Add a new chaotic interaction term with different frequency
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 8 * (1 + np.sin(self.chaotic_sequence[i] * 6))
                result += 0.05 * freq * np.sin(x[i] + x[j]) * np.cos(self.chaotic_sequence[i] * x[j])
        
        # Add a new chaotic coupling with higher frequency interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 10 * (1 + np.cos(self.chaotic_sequence[i] * 7))
                result += 0.03 * freq * np.cos(x[i] * x[j]) * np.sin(self.chaotic_sequence[j] * x[i])
        
        return result