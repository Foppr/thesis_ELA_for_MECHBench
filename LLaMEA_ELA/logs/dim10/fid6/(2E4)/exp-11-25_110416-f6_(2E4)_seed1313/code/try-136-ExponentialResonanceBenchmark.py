import numpy as np

class ExponentialResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute exponential decay sequence for adaptive conditioning
        self.decay_seq = np.exp(-np.arange(dim * 20) * 0.1)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base exponential decay term with adaptive conditioning
        result = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.6 * np.sin(self.decay_seq[i % len(self.decay_seq)] * 30)
            result += cond_factor * np.exp(-0.5 * x[i]**2) * (x[i]**4 - 2*x[i]**2 + 1)
        
        # Add trigonometric resonance patterns with dynamic frequencies
        for i in range(self.dim):
            resonance_sum = 0.0
            for k in range(1, min(6, self.dim + 1)):
                freq = k * (1 + 0.3 * np.cos(self.decay_seq[(i+k*2) % len(self.decay_seq)] * 5))
                resonance_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8) * np.sin(freq * x[i] * 0.4)
            result += 1.5 * resonance_sum
            
        # Add adaptive exponential coupling terms
        for i in range(min(15, self.dim)):
            coupling_strength = 0.7 + 0.5 * np.sin(self.decay_seq[(i*5) % len(self.decay_seq)] * 20)
            result += coupling_strength * np.exp(-x[i]**2) * np.cos(3 * x[i]) * np.sin(2 * x[i])
            
        # Add multi-scale exponential decay components
        for i in range(self.dim):
            decay_sum = 0.0
            for k in range(1, min(8, self.dim + 1)):
                scale = 1.0 / (k**1.5)
                decay_sum += scale * np.exp(-k * x[i]**2) * np.sin(k * x[i]) * np.cos(k * x[i] * 0.6)
            result += 0.8 * decay_sum
            
        # Add complex cross-dimensional exponential couplings
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling = 0.9 + 0.4 * np.sin(self.decay_seq[(i*j*3) % len(self.decay_seq)] * 12)
                result += coupling * np.exp(-0.5 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
                
        # Add enhanced basin boundary effects with varying steepness
        for i in range(self.dim):
            if abs(x[i]) < 1.2:
                result += 0.6 * (x[i]**2 - 1.44)**2
            else:
                result += 0.4 * np.abs(x[i] - np.sign(x[i]) * 1.2)**3
                
        # Add fractal-like exponential components
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(6, self.dim + 1)):
                fractal_sum += (0.2 / k**1.2) * np.exp(-k * x[i]**2) * np.sin(k**1.8 * x[i])
            result += 0.5 * fractal_sum
            
        # Add harmonic exponential terms for increased complexity
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                harmonic_coupling = 0.5 + 0.3 * np.sin(self.decay_seq[(i+j*4) % len(self.decay_seq)] * 15)
                result += harmonic_coupling * np.exp(-0.5 * (x[i]**2 + x[j]**2)) * np.cos(x[i] + x[j])
                
        # Add gradient complexity with exponential dependencies
        for i in range(self.dim):
            grad_term = 0.0
            for k in range(1, min(5, self.dim + 1)):
                grad_term += k * np.exp(-k * x[i]**2) * np.sin(k * x[i]) * np.cos(k * x[i] * 0.7)
            result += 0.6 * grad_term
            
        # Add ridge-like structures with exponential decay
        for i in range(self.dim):
            ridge_height = 0.4 + 0.3 * np.sin(self.decay_seq[(i*8) % len(self.decay_seq)] * 18)
            result += ridge_height * np.exp(-0.3 * x[i]**2) * np.cos(4 * x[i])
            
        return result