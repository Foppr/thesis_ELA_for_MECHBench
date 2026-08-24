import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic constants with enhanced complexity
        self.r = 3.8  # Slightly different logistic map parameter for more chaos
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate a more complex chaotic sequence using logistic map with offset
        seq = np.zeros(self.dim)
        x = 0.5  # Initial value
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x + 0.1 * np.sin(i * np.pi / self.dim)  # Add sinusoidal modulation
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
            exponents = [2, 3, 4, 5, 6]
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            result += chaotic_factor * (x[i]**exp - exp*x[i]**(exp-1) + (exp*(exp-1)/2)*x[i]**(exp-2))
            
        # Enhanced trigonometric coupling with multiple frequencies and chaotic amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                amp = 0.3 * (1 + np.sin(3 * phase))  # Adaptive amplitude
                freq1 = 3 * (1 + np.cos(2 * phase))
                freq2 = 2 * (1 + np.sin(2 * phase))
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Adaptive spherical penalty with chaotic center and variable radius
        center = np.array([self.chaotic_sequence[i] * 3.0 for i in range(self.dim)])
        radius = 1.5 + 0.5 * np.sin(self.chaotic_sequence[0] * 10)
        result += 0.4 * np.sum(((x - center) / radius)**2)
        
        # Multi-frequency chaotic oscillation with varying amplitudes
        for i in range(self.dim):
            freq = 15 + 10 * self.chaotic_sequence[i]
            amp = 0.15 + 0.05 * np.cos(5 * self.chaotic_sequence[i])
            result += amp * np.sin(freq * x[i])
            
        # Add global minimum attractor with chaotic scaling
        scale = 0.05 + 0.05 * np.sin(self.chaotic_sequence[0] * 20)
        result += scale * np.sum(x**2)
        
        # Add a small chaotic noise term to increase landscape complexity
        noise = 0.01 * np.sum(np.sin(self.chaotic_sequence * x))
        result += noise
        
        # Add a new chaotic modulation to improve fitness score - slightly modified coefficients
        modulate = 0.03 * np.sum(np.cos(self.chaotic_sequence * x**2))  # Increased coefficient
        result += modulate
        
        # Add a new chaotic interaction term with different frequency and amplitude
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 7 * (1 + np.sin(self.chaotic_sequence[i] * 5))
                amp = 0.04 * (1 + np.cos(self.chaotic_sequence[j] * 3))  # Different amplitude modulation
                result += amp * freq * np.sin(x[i] + x[j]) * np.cos(self.chaotic_sequence[i] * x[j])
        
        # Add a new hyper-chaotic interaction term with higher frequency components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 12 * (1 + np.sin(self.chaotic_sequence[i] * 7))
                result += 0.02 * freq * np.sin(2 * x[i] + x[j]) * np.cos(3 * self.chaotic_sequence[j] * x[i])
        
        return result