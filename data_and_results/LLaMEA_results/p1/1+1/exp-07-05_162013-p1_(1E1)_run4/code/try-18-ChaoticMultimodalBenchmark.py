import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.r = 3.9
        self.chaotic_sequence = self._generate_chaotic_sequence()
        self.fbm_exponent = 0.7
        
    def _generate_chaotic_sequence(self):
        seq = np.zeros(self.dim)
        x = 0.5
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x
        return seq
    
    def _fractional_brownian_coupling(self, x):
        # Simulate fractional Brownian motion-like coupling
        fbm = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                fbm += np.sin(2 * np.pi * dist ** self.fbm_exponent)
        return fbm
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Nested chaotic polynomial component with varying exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponent = 2 + int(chaotic_factor * 10) % 4
            result += chaotic_factor * (x[i]**exponent - exponent*x[i]**(exponent-1) + 
                                       (exponent*(exponent-1))/2 * x[i]**(exponent-2))
        
        # Trigonometric coupling with fractional Brownian motion
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                coupling = self._fractional_brownian_coupling(x)
                result += 0.3 * np.sin(3 * np.pi * x[i] + phase) * np.cos(3 * np.pi * x[j] + phase) * coupling
                
        # Adaptive spherical penalty with chaotic center and dynamic radius
        center = np.array([self.chaotic_sequence[i] * 3.0 for i in range(self.dim)])
        radius = 1.0 + 0.5 * np.mean(self.chaotic_sequence)
        result += 0.4 * np.sum((x - center)**2) / radius
        
        # Multi-scale chaotic oscillation
        for i in range(self.dim):
            scale = 1 + int(self.chaotic_sequence[i] * 20) % 5
            result += 0.15 * np.sin(scale * x[i] * self.chaotic_sequence[i] * 10)
            
        # Add a global minimum attractor with chaotic modulation
        global_min = 0.05 * np.sum(x**2)
        result += global_min * (1 + 0.3 * np.mean(self.chaotic_sequence))
        
        # Add a secondary chaotic basin with different scaling
        for i in range(self.dim):
            result += 0.25 * np.sin(5 * x[i] * self.chaotic_sequence[i] + np.pi/4) * \
                      np.cos(5 * x[i] * self.chaotic_sequence[i] + np.pi/4)
        
        return result