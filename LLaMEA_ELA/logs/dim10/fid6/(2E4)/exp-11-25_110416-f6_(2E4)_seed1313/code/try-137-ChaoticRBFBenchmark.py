import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate chaotic sequence for dynamic conditioning
        self.chaos_seq = np.array([0.1])
        for _ in range(dim * 50):
            self.chaos_seq = np.append(self.chaos_seq, 3.8 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add radial basis function components with chaotic widths and centers
        for i in range(min(15, self.dim)):
            center = 3.0 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 20)
            width = 0.5 + 0.5 * np.cos(self.chaos_seq[(i*7) % len(self.chaos_seq)] * 15)
            result += np.exp(-0.5 * ((x[i] - center) / width)**2) * (1.0 + 0.3 * np.sin(10 * x[i]))
            
        # Add sinusoidal interference patterns with dynamic frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(self.chaos_seq[(i*3) % len(self.chaos_seq)] * 8)
            amp = 1.5 + 0.5 * np.cos(self.chaos_seq[(i*5) % len(self.chaos_seq)] * 12)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
            
        # Add polynomial cross-dimensional terms with chaotic coupling strengths
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(i+1, min(i+5, self.dim)):
                coupling = 0.7 + 0.3 * np.sin(self.chaos_seq[(i+j) % len(self.chaos_seq)] * 25)
                poly_sum += coupling * x[i]**2 * x[j]**4
            result += 0.3 * poly_sum
            
        # Add chaotic noise with adaptive amplitude and frequency
        for i in range(self.dim):
            noise_amp = 0.4 + 0.2 * np.sin(self.chaos_seq[(i*13) % len(self.chaos_seq)] * 40)
            noise_freq = 5.0 + 2.0 * np.cos(self.chaos_seq[(i*9) % len(self.chaos_seq)] * 30)
            result += noise_amp * np.sin(noise_freq * x[i] + 0.5 * np.sin(20 * x[i]))
            
        # Add basin-shaped regions with varying steepness
        for i in range(self.dim):
            dist_from_center = np.abs(x[i])
            if dist_from_center < 2.0:
                result += 0.8 * (dist_from_center - 1.0)**4
            else:
                result += 0.5 * (dist_from_center - 2.0)**3
                
        # Add fractal-like self-similar oscillations
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(8, self.dim + 1)):
                scale = 1.0 / (k**1.8)
                fractal_sum += scale * np.sin(k**1.7 * x[i]) * np.cos(k**1.3 * x[i])
            result += 0.6 * fractal_sum
            
        # Add adaptive conditioning based on chaotic sequence
        condition_factor = 1.0 + 0.4 * np.sin(self.chaos_seq[0] * 50)
        result *= condition_factor
        
        return result