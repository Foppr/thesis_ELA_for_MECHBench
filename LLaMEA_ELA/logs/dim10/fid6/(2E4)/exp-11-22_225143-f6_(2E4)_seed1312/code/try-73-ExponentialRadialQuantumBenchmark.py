import numpy as np

class ExponentialRadialQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Exponential decay interaction parameters
        self.decay_rates = np.random.uniform(0.1, 2.0, dim)
        self.decay_ampls = np.random.uniform(0.5, 3.0, dim)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, dim)
        # Quantum-inspired phase transition parameters
        self.phase_freqs = np.random.uniform(1.0, 6.0, dim)
        self.phase_ampls = np.random.uniform(0.3, 1.5, dim)
        self.phase_phases = np.random.uniform(0.0, 2.0 * np.pi, dim)
        # Intermittent valley parameters
        self.valley_freqs = np.random.uniform(0.5, 3.0, 3)
        self.valley_ampls = np.random.uniform(0.1, 0.8, 3)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Exponential decay interaction terms
        for i in range(self.dim):
            decay_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(x_norm[i] - x_norm[j])
                    decay_sum += self.decay_ampls[i] * np.exp(-self.decay_rates[i] * dist)
            f_val += 0.2 * decay_sum**2
        
        # Radial basis function couplings
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                dist = np.sum((x_norm - self.rbf_centers[i, :])**2)
                rbf_sum += np.exp(-0.5 * dist / (self.rbf_widths[i]**2))
            f_val += 0.3 * rbf_sum**1.5
        
        # Quantum-inspired phase transitions
        for i in range(self.dim):
            phase_term = self.phase_ampls[i] * np.sin(self.phase_freqs[i] * x_norm[i] + self.phase_phases[i])
            f_val += 0.25 * (phase_term**2 + 0.1 * np.abs(phase_term)**3)
        
        # Intermittent valleys with multiple frequency components
        valley_sum = 0.0
        for k in range(3):
            freq_term = 0.0
            for i in range(self.dim):
                freq_term += self.valley_freqs[k] * np.cos(self.valley_freqs[k] * x_norm[i])
            valley_sum += self.valley_ampls[k] * np.sin(freq_term)
        f_val += 0.2 * valley_sum**2
        
        # Sharp fitness gradients with polynomial perturbations
        grad_pert = 0.0
        for i in range(self.dim):
            grad_pert += (x_norm[i]**5 - 2.0 * x_norm[i]**3 + x_norm[i])
        f_val += 0.15 * np.abs(grad_pert)**1.8
        
        # Add non-uniform noise with exponential scaling
        noise_pert = 0.0
        for i in range(self.dim):
            noise_pert += np.exp(-x_norm[i]**2) * np.sin(3.0 * x_norm[i])
        f_val += 0.1 * noise_pert**2
        
        return f_val