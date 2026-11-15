import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.r = 3.9
        self.chaotic_sequence = self._generate_chaotic_sequence()
        self.fbm_sequence = self._generate_fbm_sequence()
        
    def _generate_chaotic_sequence(self):
        seq = np.zeros(self.dim)
        x = 0.5
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x
        return seq
    
    def _generate_fbm_sequence(self):
        # Generate fractional Brownian motion-like sequence
        seq = np.zeros(self.dim)
        for i in range(self.dim):
            seq[i] = np.sin(i * 0.1) * np.cos(i * 0.05) + np.random.normal(0, 0.1)
        return seq
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Nested chaotic polynomial component with dynamic exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponent = 2 + 2 * chaotic_factor
            result += chaotic_factor * (x[i]**exponent - exponent*x[i]**(exponent-1) + 
                                       (exponent*(exponent-1)/2)*x[i]**(exponent-2))
            
        # Fractional Brownian motion coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fbm_phase = self.fbm_sequence[i] * self.fbm_sequence[j]
                result += 0.3 * np.sin(3 * np.pi * x[i] + fbm_phase) * np.cos(3 * np.pi * x[j] + fbm_phase)
                
        # Dynamic saddle-point penalty with chaotic scaling
        for i in range(self.dim):
            saddle_scale = 1.0 + 0.5 * self.chaotic_sequence[i]
            result += saddle_scale * (x[i]**2 - 4*x[i] + 4) * (x[i]**2 + 4*x[i] + 4)
            
        # High-frequency chaotic oscillation with time-varying frequency
        for i in range(self.dim):
            freq = 15 + 10 * self.chaotic_sequence[i]
            result += 0.15 * np.sin(freq * x[i] * self.chaotic_sequence[i])
            
        # Add chaotic global minimum attractor with dynamic center
        center = np.array([self.chaotic_sequence[i] * 1.5 for i in range(self.dim)])
        result += 0.2 * np.sum((x - center)**2)
        
        # Add a chaotic noise component
        noise = np.sum([self.chaotic_sequence[i] * np.sin(5 * x[i]) for i in range(self.dim)])
        result += 0.05 * noise
        
        return result