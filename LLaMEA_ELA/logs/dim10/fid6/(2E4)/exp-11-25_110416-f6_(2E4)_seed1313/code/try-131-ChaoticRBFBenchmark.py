import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic conditioning
        self.chaos_seq = np.array([0.5])
        for _ in range(dim * 50):
            self.chaos_seq = np.append(self.chaos_seq, 4 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial basis function component
        result = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(min(10, self.dim)):
                # Dynamic center and width based on chaotic sequence
                center = 3 * np.sin(self.chaos_seq[(i+j*7) % len(self.chaos_seq)])
                width = 0.5 + 0.5 * np.cos(self.chaos_seq[(i*j*3) % len(self.chaos_seq)])
                rbf_sum += np.exp(-0.5 * ((x[i] - center) / width)**2)
            result += rbf_sum
            
        # Add sinusoidal interference patterns
        for i in range(self.dim):
            sin_sum = 0.0
            for k in range(1, min(6, self.dim + 1)):
                freq = k * (1 + 0.3 * np.sin(self.chaos_seq[(i+k*2) % len(self.chaos_seq)] * 5))
                amp = 1.0 + 0.5 * np.cos(self.chaos_seq[(i*k*4) % len(self.chaos_seq)] * 3)
                sin_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8)
            result += 0.8 * sin_sum
            
        # Add cross-dimensional coupling with chaotic interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling = 2.0 + 1.5 * np.sin(self.chaos_seq[(i*j*13) % len(self.chaos_seq)] * 7)
                result += coupling * np.sin(x[i] * x[j]) * np.cos(x[i] * x[j] * 0.5)
                
        # Add polynomial chaos components with dynamic exponents
        for i in range(min(15, self.dim)):
            exp_factor = 2 + 3 * np.sin(self.chaos_seq[(i*11) % len(self.chaos_seq)] * 2)
            result += 0.3 * (x[i]**exp_factor) * np.sin(4 * x[i])
            
        # Add basin boundary effects with varying steepness
        for i in range(self.dim):
            if abs(x[i]) < 1.5:
                result += 0.6 * (x[i]**2 - 1)**2
            else:
                result += 0.4 * np.abs(x[i] - np.sign(x[i]) * 1.5)**3
                
        # Add multi-scale oscillatory components with varying amplitudes
        for i in range(self.dim):
            osc_sum = 0.0
            for k in range(1, min(8, self.dim + 1)):
                amp = 0.5 + 0.3 * np.sin(self.chaos_seq[(i+k*5) % len(self.chaos_seq)] * 4)
                osc_sum += amp * np.sin(k * x[i]) * np.cos(k * x[i] * 0.3)
            result += 0.7 * osc_sum
            
        # Add fractal-like self-similar components
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(6, self.dim + 1)):
                fractal_sum += (0.2 / k**1.5) * np.sin(k**1.8 * x[i]) * np.cos(k**1.2 * x[i])
            result += 0.5 * fractal_sum
            
        return result