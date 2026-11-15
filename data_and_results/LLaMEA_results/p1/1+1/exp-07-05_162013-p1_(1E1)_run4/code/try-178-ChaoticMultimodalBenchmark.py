import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced hyperchaotic constants with nested sequences
        self.r1 = 3.9
        self.r2 = 3.7
        self.chaotic_sequence = self._generate_chaotic_sequence()
        self.nested_sequence = self._generate_nested_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate primary chaotic sequence using logistic map
        seq = np.zeros(self.dim)
        x = 0.5
        for i in range(self.dim):
            x = self.r1 * x * (1 - x)
            seq[i] = x
        return seq
    
    def _generate_nested_sequence(self):
        # Generate nested chaotic sequence for higher complexity
        seq = np.zeros(self.dim)
        x = 0.3
        for i in range(self.dim):
            x = self.r2 * x * (1 - x)
            seq[i] = x + 0.05 * np.sin(i * np.pi / self.dim)
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Hyperchaotic polynomial component with nested exponents
        for i in range(self.dim):
            chaotic_factor1 = self.chaotic_sequence[i]
            chaotic_factor2 = self.nested_sequence[i]
            # Use nested chaotic exponents
            exponents = [2, 3, 4, 5, 6, 7, 8]
            exp_idx1 = int(chaotic_factor1 * len(exponents)) % len(exponents)
            exp_idx2 = int(chaotic_factor2 * len(exponents)) % len(exponents)
            exp = exponents[exp_idx1] + exponents[exp_idx2] // 2
            result += chaotic_factor1 * (x[i]**exp - exp*x[i]**(exp-1) + (exp*(exp-1)/2)*x[i]**(exp-2))
            
        # Multi-scale trigonometric coupling with dynamic frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.nested_sequence[j]
                amp = 0.4 * (1 + np.sin(4 * phase)) * (1 + np.cos(2 * phase))
                freq1 = 4 * (1 + np.cos(3 * phase))
                freq2 = 3 * (1 + np.sin(3 * phase))
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Dynamic spherical penalty with nested chaotic center and radius
        center = np.array([self.chaotic_sequence[i] * 4.0 + self.nested_sequence[i] * 2.0 for i in range(self.dim)])
        radius = 1.5 + 1.0 * np.sin(self.chaotic_sequence[0] * 15) * np.cos(self.nested_sequence[0] * 10)
        result += 0.5 * np.sum(((x - center) / radius)**2)
        
        # Multi-frequency hyperchaotic oscillation with variable amplitudes
        for i in range(self.dim):
            freq = 20 + 15 * self.chaotic_sequence[i] + 10 * self.nested_sequence[i]
            amp = 0.2 + 0.1 * np.cos(7 * self.chaotic_sequence[i]) * np.sin(5 * self.nested_sequence[i])
            result += amp * np.sin(freq * x[i])
            
        # Add global minimum attractor with hyperchaotic scaling
        scale = 0.08 + 0.04 * np.sin(self.chaotic_sequence[0] * 25) * np.cos(self.nested_sequence[0] * 20)
        result += scale * np.sum(x**2)
        
        # Add hyperchaotic noise term
        noise = 0.02 * np.sum(np.sin(self.chaotic_sequence * x) * np.cos(self.nested_sequence * x))
        result += noise
        
        # Add nested chaotic modulation
        modulate = 0.05 * np.sum(np.cos(self.chaotic_sequence * x**2) * np.sin(self.nested_sequence * x**2))
        result += modulate
        
        # Add nested chaotic interaction terms - enhanced with additional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq1 = 10 * (1 + np.sin(self.chaotic_sequence[i] * 10))
                freq2 = 8 * (1 + np.cos(self.nested_sequence[i] * 8))
                result += 0.06 * freq1 * freq2 * np.sin(x[i] + x[j]) * np.cos(self.chaotic_sequence[i] * x[j] + self.nested_sequence[j] * x[i])
        
        # Add nested hyperchaotic coupling term - enhanced with additional frequency modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 6 * (1 + np.cos(self.chaotic_sequence[i] * 6)) * (1 + np.sin(self.nested_sequence[i] * 6))
                result += 0.07 * freq * np.sin(x[i] * x[j]) * np.sin(self.chaotic_sequence[i] * x[j] + self.nested_sequence[j] * x[i])
        
        # Add nested polynomial chaos interaction - enhanced with additional nonlinearity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * (x[i]**4 + x[j]**4) * np.cos(self.chaotic_sequence[i] * x[j] + self.nested_sequence[i] * x[j])
        
        # Add nested sinusoidal coupling with variable phase shifts - enhanced with chaotic modulation
        for i in range(self.dim):
            phase_shift = 0.6 * np.sin(self.chaotic_sequence[i] * 10) + 0.4 * np.cos(self.nested_sequence[i] * 10)
            result += 0.04 * np.sin(5 * x[i] + phase_shift) * np.cos(4 * x[i] + phase_shift)
        
        # Add nested chaotic higher-order interaction - enhanced with additional chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    freq = 5 * (1 + np.sin(self.chaotic_sequence[i] * 5)) * (1 + np.cos(self.nested_sequence[j] * 5))
                    result += 0.02 * freq * np.sin(x[i] + x[j] + x[k]) * np.cos(self.chaotic_sequence[i] * x[j] + self.nested_sequence[j] * x[k])
        
        # Add nested chaotic trigonometric coupling - enhanced with additional chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * np.sin(self.chaotic_sequence[i] * x[i] + self.nested_sequence[j] * x[j]) * np.cos(self.nested_sequence[i] * x[i] + self.chaotic_sequence[j] * x[j])
        
        # Add enhanced chaotic interaction terms with additional complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    freq1 = 3 * (1 + np.sin(self.chaotic_sequence[i] * 3))
                    freq2 = 4 * (1 + np.cos(self.nested_sequence[j] * 4))
                    freq3 = 2 * (1 + np.sin(self.chaotic_sequence[k] * 2))
                    result += 0.015 * freq1 * freq2 * freq3 * np.sin(x[i] * x[j] * x[k]) * np.cos(self.chaotic_sequence[i] * x[j] + self.nested_sequence[j] * x[k])
        
        # Add enhanced nested chaotic coupling with dynamic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scaling = 0.02 * (1 + np.sin(self.chaotic_sequence[i] * 12)) * (1 + np.cos(self.nested_sequence[j] * 12))
                result += scaling * np.sin(self.chaotic_sequence[i] * x[i] + self.nested_sequence[j] * x[j]) * np.cos(self.nested_sequence[i] * x[i] + self.chaotic_sequence[j] * x[j])
        
        # Add enhanced polynomial chaos with dynamic exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp1 = 2 + int(3 * self.chaotic_sequence[i])
                exp2 = 2 + int(3 * self.nested_sequence[j])
                result += 0.025 * (x[i]**exp1 + x[j]**exp2) * np.sin(self.chaotic_sequence[i] * x[j] + self.nested_sequence[i] * x[j])
        
        # Add enhanced multi-scale oscillation with chaotic frequency
        for i in range(self.dim):
            freq = 25 + 15 * self.chaotic_sequence[i] + 10 * self.nested_sequence[i]
            amp = 0.15 + 0.05 * np.sin(5 * self.chaotic_sequence[i]) * np.cos(3 * self.nested_sequence[i])
            result += amp * np.sin(freq * x[i] + self.chaotic_sequence[i] * self.nested_sequence[i])
        
        # Slight modification: Increase the influence of the chaotic interaction terms by 15%
        result *= 1.15
        
        return result