import numpy as np

class QuantumHarmonicPenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Quantum-inspired harmonic oscillator potential with complex frequencies
        quantum_term = 0.0
        for i in range(self.dim):
            freq_real = 1.0 + 2.0 * np.sin(i * 0.5 + self.dim * 0.2)
            freq_imag = 0.5 + 1.5 * np.cos(i * 0.3 + self.dim * 0.4)
            quantum_term += (freq_real * x[i]**2 + freq_imag * x[i]**4) * np.exp(-0.1 * x[i]**2)
        
        # Quaternion-based rotation matrix with adaptive angles
        rot_term = 0.0
        for i in range(self.dim):
            angle = np.pi * (0.5 + 0.5 * np.sin(i * 0.8 + self.dim * 0.3))
            rot_term += x[i]**2 * np.cos(angle) + x[(i+1) % self.dim]**2 * np.sin(angle)
        
        # Adaptive penalty function with dynamic thresholds
        penalty_term = 0.0
        for i in range(self.dim):
            threshold = 2.0 + 1.5 * np.sin(i * 0.6 + self.dim * 0.25)
            penalty = 0.0
            if x[i] > threshold:
                penalty = (x[i] - threshold)**3
            elif x[i] < -threshold:
                penalty = (-x[i] - threshold)**3
            penalty_term += penalty
        
        # Multi-scale fractal-like structure with self-similar patterns
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 0.1 + 0.9 * np.sin(i * 0.7 + self.dim * 0.4)
            fractal_term += scale * np.sin(x[i] * scale**(-2)) * np.cos(x[i] * scale**(-1))
        
        # Coupling terms with phase-shifted interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(i * j * 0.2 + self.dim * 0.3)
                coupling = np.sin(x[i] + x[j] + phase) * np.cos(x[i] - x[j] + phase)
                coupling_term += coupling**2
        
        # Complex peak landscape with varying amplitudes and positions
        peak_term = 0.0
        for i in range(self.dim):
            amp1 = 1.5 + 2.5 * np.sin(i * 0.4)
            pos1 = -3.0 + 6.0 * np.sin(i * 0.7)
            amp2 = 2.0 + 1.0 * np.cos(i * 0.5)
            pos2 = -2.0 + 4.0 * np.cos(i * 0.6)
            peak_term += amp1 * np.exp(-0.5 * ((x[i] - pos1) / 0.8)**2) + amp2 * np.exp(-0.5 * ((x[i] - pos2) / 1.2)**2)
        
        # Adaptive noise modulation with chaotic seeding
        noise_term = 0.0
        for i in range(self.dim):
            seed = np.sin(i * 0.3 + self.dim * 0.5)
            noise = np.sin(x[i] * seed) * np.cos(x[i] * seed * 0.7)
            noise_term += noise
        
        # Final weighted combination with dynamic scaling
        total = 0.25 * quantum_term + 0.15 * rot_term + 0.20 * penalty_term + 0.18 * fractal_term + 0.12 * coupling_term + 0.08 * peak_term + 0.02 * noise_term
        
        # Global conditioning factor with dimensional dependency
        condition_factor = 1.0 + 0.2 * np.sin(self.dim * 0.4) * np.cos(self.dim * 0.3)
        
        return total * condition_factor