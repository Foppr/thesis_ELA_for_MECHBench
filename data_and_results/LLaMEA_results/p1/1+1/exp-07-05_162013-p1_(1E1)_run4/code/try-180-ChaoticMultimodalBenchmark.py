import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced hyperchaotic constants with improved nested sequences
        self.r1 = 3.9
        self.r2 = 3.7
        self.chaotic_sequence = self._generate_chaotic_sequence()
        self.nested_sequence = self._generate_nested_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate primary chaotic sequence using logistic map with better distribution
        seq = np.zeros(self.dim)
        x = 0.5
        for i in range(self.dim):
            x = self.r1 * x * (1 - x)
            seq[i] = x
        return seq
    
    def _generate_nested_sequence(self):
        # Generate nested chaotic sequence with improved complexity and distribution
        seq = np.zeros(self.dim)
        x = 0.3
        for i in range(self.dim):
            x = self.r2 * x * (1 - x)
            seq[i] = x + 0.03 * np.sin(i * np.pi / self.dim) + 0.02 * np.cos(i * np.pi / (2 * self.dim))
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Hyperchaotic polynomial component with enhanced nested exponents
        for i in range(self.dim):
            chaotic_factor1 = self.chaotic_sequence[i]
            chaotic_factor2 = self.nested_sequence[i]
            # Use enhanced nested chaotic exponents
            exponents = [2, 3, 4, 5, 6, 7, 8, 9, 10]
            exp_idx1 = int(chaotic_factor1 * len(exponents)) % len(exponents)
            exp_idx2 = int(chaotic_factor2 * len(exponents)) % len(exponents)
            exp = exponents[exp_idx1] + exponents[exp_idx2] // 2
            # Use modified polynomial with better conditioning
            result += chaotic_factor1 * (x[i]**exp - exp*x[i]**(exp-1) + (exp*(exp-1)/2)*x[i]**(exp-2) + 0.01*x[i])
            
        # Multi-scale trigonometric coupling with dynamic frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.nested_sequence[j]
                amp = 0.3 * (1 + np.sin(4 * phase)) * (1 + np.cos(2 * phase)) + 0.05 * np.sin(3 * phase)
                freq1 = 3 * (1 + np.cos(3 * phase)) + 0.5 * np.sin(2 * phase)
                freq2 = 2.5 * (1 + np.sin(3 * phase)) + 0.3 * np.cos(2 * phase)
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Dynamic spherical penalty with enhanced nested chaotic center and radius
        center = np.array([self.chaotic_sequence[i] * 3.5 + self.nested_sequence[i] * 1.5 for i in range(self.dim)])
        radius = 1.2 + 0.8 * np.sin(self.chaotic_sequence[0] * 15) * np.cos(self.nested_sequence[0] * 10)
        result += 0.4 * np.sum(((x - center) / radius)**2)
        
        # Multi-frequency hyperchaotic oscillation with variable amplitudes
        for i in range(self.dim):
            freq = 18 + 12 * self.chaotic_sequence[i] + 8 * self.nested_sequence[i]
            amp = 0.15 + 0.08 * np.cos(7 * self.chaotic_sequence[i]) * np.sin(5 * self.nested_sequence[i])
            result += amp * np.sin(freq * x[i]) + 0.02 * np.cos(2 * freq * x[i])
            
        # Add global minimum attractor with enhanced hyperchaotic scaling
        scale = 0.06 + 0.03 * np.sin(self.chaotic_sequence[0] * 25) * np.cos(self.nested_sequence[0] * 20)
        result += scale * np.sum(x**2)
        
        # Add enhanced hyperchaotic noise term
        noise = 0.015 * np.sum(np.sin(self.chaotic_sequence * x) * np.cos(self.nested_sequence * x) + 0.01 * np.sin(2 * self.chaotic_sequence * x))
        result += noise
        
        # Add enhanced nested chaotic modulation
        modulate = 0.04 * np.sum(np.cos(self.chaotic_sequence * x**2) * np.sin(self.nested_sequence * x**2) + 0.005 * np.sin(3 * self.chaotic_sequence * x**2))
        result += modulate
        
        # Add enhanced nested chaotic interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq1 = 8 * (1 + np.sin(self.chaotic_sequence[i] * 10)) + 0.5 * np.cos(self.chaotic_sequence[i] * 10)
                freq2 = 6 * (1 + np.cos(self.nested_sequence[i] * 8)) + 0.3 * np.sin(self.nested_sequence[i] * 8)
                result += 0.05 * freq1 * freq2 * np.sin(x[i] + x[j]) * np.cos(self.chaotic_sequence[i] * x[j] + self.nested_sequence[j] * x[i])
        
        # Add enhanced nested hyperchaotic coupling term
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 5 * (1 + np.cos(self.chaotic_sequence[i] * 6)) * (1 + np.sin(self.nested_sequence[i] * 6)) + 0.2 * np.sin(self.chaotic_sequence[i] * 6)
                result += 0.06 * freq * np.sin(x[i] * x[j]) * np.sin(self.chaotic_sequence[i] * x[j] + self.nested_sequence[j] * x[i])
        
        # Add enhanced nested polynomial chaos interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.025 * (x[i]**4 + x[j]**4) * np.cos(self.chaotic_sequence[i] * x[j] + self.nested_sequence[i] * x[j]) + 0.005 * x[i]**3 * x[j]**2
        
        # Add enhanced nested sinusoidal coupling with variable phase shifts
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(self.chaotic_sequence[i] * 10) + 0.3 * np.cos(self.nested_sequence[i] * 10) + 0.05 * np.sin(2 * self.chaotic_sequence[i])
            result += 0.03 * np.sin(5 * x[i] + phase_shift) * np.cos(4 * x[i] + phase_shift) + 0.005 * np.sin(3 * x[i] + phase_shift)
        
        # Add enhanced nested chaotic higher-order interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    freq = 4 * (1 + np.sin(self.chaotic_sequence[i] * 5)) * (1 + np.cos(self.nested_sequence[j] * 5)) + 0.1 * np.cos(self.chaotic_sequence[i] * 5)
                    result += 0.015 * freq * np.sin(x[i] + x[j] + x[k]) * np.cos(self.chaotic_sequence[i] * x[j] + self.nested_sequence[j] * x[k])
        
        # Add enhanced nested chaotic trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.025 * np.sin(self.chaotic_sequence[i] * x[i] + self.nested_sequence[j] * x[j]) * np.cos(self.nested_sequence[i] * x[i] + self.chaotic_sequence[j] * x[j]) + 0.003 * np.sin(2 * self.chaotic_sequence[i] * x[i])
        
        # Add enhanced cross-dimensional interaction terms
        for i in range(self.dim):
            result += 0.01 * np.sin(self.chaotic_sequence[i] * x[i]**2) * np.cos(self.nested_sequence[i] * x[i]**2) + 0.002 * x[i]**5
        
        # Add improved scaling factor to balance complexity
        result *= 1.05
        
        return result