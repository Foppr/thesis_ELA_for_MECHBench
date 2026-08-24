import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequences for dynamic shifts, scaling, and frequency modulation
        self.chaotic_sequence = np.sin(np.arange(dim) * np.pi / 2.7) * 0.5 + 0.5
        self.freq_sequence = np.cos(np.arange(dim) * np.pi / 2.2) * 0.4 + 0.6
        self.phase_sequence = np.tan(np.arange(dim) * np.pi / 4.1) * 0.3 + 0.7
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial terms with chaotic coefficients
        result = 0.0
        for i in range(self.dim):
            coeff1 = 0.7 + 0.3 * self.chaotic_sequence[i]
            coeff2 = 0.5 + 0.2 * self.freq_sequence[i]
            result += coeff1 * (x[i] - 1.0)**2 + coeff2 * (x[i] + 1.3)**2 + 0.02 * x[i]**4 + 0.003 * x[i]**7
        
        # Chaotic interaction terms with dynamic scaling, phase shifts, and non-linear coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_scale = 2.0 + 4.0 * self.chaotic_sequence[i] * self.chaotic_sequence[j]
                phase_shift = self.chaotic_sequence[i] * self.phase_sequence[j]
                coupling = np.sin(3.0 * (x[i] - x[j]) + phase_shift) * np.cos(2.0 * (x[i] + x[j]))
                result += dynamic_scale * (x[i] - x[j])**2 * coupling
        
        # Add chaotic sinusoidal components with varying frequencies, amplitudes, and phase modulations
        for i in range(self.dim):
            freq1 = 3.0 + 2.0 * self.freq_sequence[i]
            freq2 = 4.0 + 1.5 * self.chaotic_sequence[i]
            amp1 = 1.0 + 0.3 * self.chaotic_sequence[i]
            amp2 = 0.6 + 0.4 * self.freq_sequence[i]
            phase1 = self.chaotic_sequence[i] * np.pi / 2.0
            phase2 = self.phase_sequence[i] * np.pi / 3.0
            result += amp1 * np.sin(freq1 * x[i] + phase1) * np.cos(freq2 * x[i] + phase2) + \
                      amp2 * np.sin(freq1 * x[i] + phase1**2) * np.cos(freq2 * x[i] + phase2**2)
        
        # Add a global minimum shift based on chaotic sequence with non-linear transformation
        shift = np.array([self.chaotic_sequence[i] * 0.5 * np.sin(self.chaotic_sequence[i] * np.pi) for i in range(self.dim)])
        result += 0.2 * np.sum((x - shift)**2)
        
        # Add high-frequency noise with chaotic modulation and dynamic amplitude
        noise = 0.0
        for i in range(self.dim):
            amp = 0.1 + 0.05 * self.chaotic_sequence[i] * self.freq_sequence[i]
            noise += amp * np.sin(30.0 * x[i]) * np.cos(25.0 * x[i]) * (1.0 + 0.3 * np.sin(self.phase_sequence[i]))
        result += noise
        
        # Add complex polynomial term with mixed degrees and chaotic coefficients
        result += 0.003 * np.sum(x**3) + 0.0015 * np.sum(x**5) + 0.001 * np.sum(x**7) + 0.0007 * np.sum(x**9) + 0.0005 * np.sum(x**11)
        
        # Add a chaotic perturbation term with dynamic frequency and amplitude
        perturbation = 0.0
        for i in range(self.dim):
            freq = 12.0 + 8.0 * self.chaotic_sequence[i]
            amp = 0.05 + 0.03 * self.freq_sequence[i]
            perturbation += amp * np.sin(freq * x[i] + self.chaotic_sequence[i] * np.pi) * np.cos(freq * x[i] + self.phase_sequence[i] * np.pi)
        result += perturbation
        
        # Add a novel chaotic cross-term interaction with dynamic coupling strength
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 1.5 + 2.5 * self.chaotic_sequence[i] * self.freq_sequence[j]
                cross_term += coupling_strength * np.sin(x[i] * x[j] + self.phase_sequence[i] + self.phase_sequence[j])
        result += cross_term
        
        # Add a modified chaotic modulation to improve performance
        mod_term = 0.0
        for i in range(self.dim):
            mod_amp = 0.02 + 0.01 * self.chaotic_sequence[i]
            mod_freq = 5.0 + 3.0 * self.freq_sequence[i]
            mod_term += mod_amp * np.sin(mod_freq * x[i]) * np.cos(mod_freq * x[i] + self.phase_sequence[i])
        result += mod_term
        
        return result