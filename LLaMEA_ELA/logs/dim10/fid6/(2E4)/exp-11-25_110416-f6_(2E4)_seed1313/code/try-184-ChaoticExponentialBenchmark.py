import numpy as np

class ChaoticExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic conditioning
        self.chaos_seq = np.array([0.1])
        for _ in range(dim * 50):
            self.chaos_seq = np.append(self.chaos_seq, 3.8 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial with chaotic conditioning
        result = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 1.5 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 60)
            result += cond_factor * (x[i]**4 - 2*x[i]**2 + 1)
            
        # Add exponential coupling components
        for i in range(self.dim):
            exp_sum = 0.0
            for j in range(min(5, self.dim)):
                if i != j:
                    coupling = 2.0 + np.sin(self.chaos_seq[(i*j*7) % len(self.chaos_seq)] * 40)
                    exp_sum += coupling * np.exp(-0.5 * (x[i] - x[j])**2)
            result += 1.5 * exp_sum
            
        # Add trigonometric interference with dynamic frequencies
        for i in range(self.dim):
            trig_sum = 0.0
            for k in range(1, min(8, self.dim + 1)):
                freq = k * (1.5 + 0.5 * np.cos(self.chaos_seq[(i+k*3) % len(self.chaos_seq)]))
                trig_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
            result += 2.0 * trig_sum
            
        # Add fractal-like polynomial components with varying exponents
        for i in range(self.dim):
            poly_sum = 0.0
            for k in range(1, min(6, self.dim + 1)):
                exp = 3 + 2 * np.sin(self.chaos_seq[(i+k*5) % len(self.chaos_seq)] * 80)
                poly_sum += (x[i]**exp) * np.cos(k * x[i])
            result += 1.2 * poly_sum
            
        # Add cross-dimensional exponential interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                coupling = 1.0 + 0.8 * np.sin(self.chaos_seq[(i*j*11) % len(self.chaos_seq)] * 50)
                result += coupling * np.exp(-0.3 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
                
        # Add chaotic modulation with dynamic amplitude
        for i in range(self.dim):
            amp = 1.0 + 1.2 * np.sin(self.chaos_seq[(i*13) % len(self.chaos_seq)] * 90)
            result += amp * np.sin(5 * x[i]) * np.cos(7 * x[i])
            
        # Add basin boundary with varying steepness
        for i in range(self.dim):
            if abs(x[i]) < 2.5:
                result += 2.5 * (x[i]**2 - 1)**4
            else:
                result += 1.8 * np.abs(x[i] - np.sign(x[i]) * 2.5)**6
                
        # Add multi-scale oscillation components
        for i in range(self.dim):
            osc_sum = 0.0
            for k in range(1, min(10, self.dim + 1)):
                scale = 1.0 / (k**2.5)
                osc_sum += scale * np.sin(k * x[i]) * np.cos(k * x[i] * 0.5)
            result += 1.3 * osc_sum
            
        # Add exponential decay with chaotic scaling
        for i in range(self.dim):
            decay_sum = 0.0
            for k in range(1, min(7, self.dim + 1)):
                scale = np.exp(-k * 0.3)
                decay_sum += scale * np.sin(k * x[i]**2)
            result += 1.6 * decay_sum
            
        return result