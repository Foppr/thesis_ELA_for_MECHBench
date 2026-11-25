import numpy as np

class ChaoticSineWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic conditioning
        self.chaos_seq = np.array([0.3])
        for _ in range(dim * 150):
            self.chaos_seq = np.append(self.chaos_seq, 3.8 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic sine-wave component with dynamic exponents
        result = 0.0
        for i in range(self.dim):
            exp_factor = 2 + 3 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 30)
            result += 0.5 * np.sin(x[i] * exp_factor) * np.cos(x[i] * 0.7 * exp_factor)
            
        # Add multi-scale sine-wave interference with varying frequencies
        for i in range(self.dim):
            wave_sum = 0.0
            for k in range(1, min(30, self.dim + 1)):  # Increased range
                freq = k * (1.2 + 0.6 * np.cos(self.chaos_seq[(i+k*3) % len(self.chaos_seq)]))
                wave_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            result += 1.5 * wave_sum
            
        # Add dynamic polynomial terms with chaotic conditioning
        for i in range(self.dim):
            cond_factor = 1.0 + 0.8 * np.sin(self.chaos_seq[(i*7) % len(self.chaos_seq)] * 50)
            result += cond_factor * (x[i]**5 - 2.0 * x[i]**3 + x[i])
            
        # Add cross-dimensional coupling with chaotic interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                coupling = 0.8 + 0.7 * np.sin(self.chaos_seq[(i*j*2) % len(self.chaos_seq)] * 40)
                result += coupling * x[i]**3 * x[j]**3
                
        # Add fractal-like oscillatory components with recursive scaling
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(25, self.dim + 1)):  # Increased range
                scale = 1.0 / (k**2.5)
                fractal_sum += scale * np.sin(k**3.0 * x[i]) * np.cos(k**2.0 * x[i])
            result += 0.8 * fractal_sum
            
        # Add basin boundary effects with varying steepness
        for i in range(self.dim):
            if abs(x[i]) < 1.5:
                result += 2.0 * (x[i]**2 - 0.5)**3
            else:
                result += 1.5 * np.abs(x[i] - np.sign(x[i]) * 1.5)**4
                
        # Add chaotic noise modulation with dynamic amplitude
        for i in range(self.dim):
            noise_amp = 0.9 + 0.7 * np.sin(self.chaos_seq[(i*13) % len(self.chaos_seq)] * 70)
            result += noise_amp * np.sin(50 * x[i]**2)
            
        # Add complex multi-modal sine-wave components
        for i in range(self.dim):
            multimodal_sum = 0.0
            for k in range(1, min(20, self.dim + 1)):  # Increased range
                amp = 0.9 + 0.5 * np.sin(self.chaos_seq[(i+k*5) % len(self.chaos_seq)] * 25)
                freq = k * (1.5 + 0.5 * np.cos(self.chaos_seq[(i+k*8) % len(self.chaos_seq)]))
                multimodal_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4)
            result += 1.2 * multimodal_sum
            
        # Add exponential cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                exp_coupling = np.exp(-0.2 * abs(x[i] - x[j]))
                result += 1.1 * exp_coupling * (x[i]**2 + x[j]**2) * np.sin(2 * x[i] * x[j])
                
        # Add enhanced chaotic modulation with frequency mixing
        for i in range(self.dim):
            chaos_mod = 0.6 + 0.7 * np.sin(self.chaos_seq[(i*17) % len(self.chaos_seq)] * 90)
            result += chaos_mod * np.sin(80 * x[i]) * np.cos(35 * x[i]**2)
            
        # Add higher-order polynomial interactions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                result += 0.6 * (x[i]**4 + x[j]**4) * np.sin(x[i] * x[j])
                
        # Add adaptive chaotic modulation with dynamic frequency
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(self.chaos_seq[(i*23) % len(self.chaos_seq)] * 80)
            result += 0.7 * np.sin(freq_mod * x[i]**3) * np.cos(freq_mod * x[i])
            
        return result