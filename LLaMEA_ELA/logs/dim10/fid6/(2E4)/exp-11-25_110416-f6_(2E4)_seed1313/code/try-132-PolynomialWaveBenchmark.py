import numpy as np

class PolynomialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for adaptive conditioning
        self.chaos_seq = np.array([0.5])
        for _ in range(dim * 30):
            self.chaos_seq = np.append(self.chaos_seq, 4 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with enhanced adaptive conditioning
        result = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.8 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 25)
            result += cond_factor * x[i]**6 - 3 * x[i]**4 + 2 * x[i]**2
        
        # Add enhanced trigonometric wave interference patterns
        for i in range(self.dim):
            wave_sum = 0.0
            for k in range(1, min(8, self.dim + 1)):
                freq = k * (1 + 0.5 * np.cos(self.chaos_seq[(i+k) % len(self.chaos_seq)] * 2))
                wave_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.sin(freq * x[i] * 0.3)
            result += 1.2 * wave_sum
            
        # Add enhanced polynomial chaos components with dynamic exponents
        for i in range(min(20, self.dim)):
            exp_factor = 3 + 4 * np.sin(self.chaos_seq[(i*9) % len(self.chaos_seq)] * 1.5)
            result += 0.5 * (x[i] ** exp_factor) * np.cos(5 * x[i]) * np.sin(2 * x[i])
            
        # Add complex cross-dimensional coupling with dynamic strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                coupling = 0.8 + 0.4 * np.sin(self.chaos_seq[(i*j*2) % len(self.chaos_seq)] * 15)
                result += coupling * x[i]**3 * x[j]**3
                
        # Add multi-scale oscillatory components with enhanced frequency modulation
        for i in range(self.dim):
            osc_sum = 0.0
            for k in range(1, min(10, self.dim + 1)):
                scale = 1.0 / (k**2)
                osc_sum += scale * np.sin(k * x[i]) * np.cos(k * x[i] * 0.5) * np.sin(k * x[i] * 0.2)
            result += 0.6 * osc_sum
            
        # Add adaptive noise with enhanced amplitude modulation
        for i in range(self.dim):
            noise_amp = 0.3 + 0.2 * np.sin(self.chaos_seq[(i*17) % len(self.chaos_seq)] * 60)
            result += noise_amp * np.sin(30 * x[i]) * np.cos(15 * x[i])
            
        # Add enhanced basin boundary regions with varying steepness
        for i in range(self.dim):
            if abs(x[i]) < 0.8:
                result += 0.8 * (x[i]**2 - 1)**3
            else:
                result += 0.5 * np.abs(x[i] - np.sign(x[i]) * 0.8)**4
                
        # Add fractal-like self-similar components
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(5, self.dim + 1)):
                fractal_sum += (0.1 / k) * np.sin(k**2 * x[i]) * np.cos(k**1.5 * x[i])
            result += 0.4 * fractal_sum
            
        # Add enhanced harmonic coupling terms for increased complexity
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                harmonic_coupling = 0.6 + 0.3 * np.sin(self.chaos_seq[(i+j*3) % len(self.chaos_seq)] * 20)
                result += harmonic_coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Add enhanced gradient complexity with directional dependencies
        for i in range(self.dim):
            grad_term = 0.0
            for k in range(1, min(6, self.dim + 1)):
                grad_term += k * np.sin(k * x[i]) * np.cos(k * x[i] * 0.8)
            result += 0.7 * grad_term
            
        # Add enhanced ridge-like structures with variable heights
        for i in range(self.dim):
            ridge_height = 0.5 + 0.3 * np.sin(self.chaos_seq[(i*7) % len(self.chaos_seq)] * 10)
            result += ridge_height * np.exp(-0.5 * x[i]**2) * np.cos(3 * x[i])
            
        return result