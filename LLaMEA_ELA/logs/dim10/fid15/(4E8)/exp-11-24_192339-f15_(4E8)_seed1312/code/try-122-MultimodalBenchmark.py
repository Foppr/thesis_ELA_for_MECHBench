import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component
        sphere = np.sum(x**2)
        
        # Enhanced chaotic sine modulations with dynamic frequency scaling and amplitude modulation
        chaotic_mod = 0
        for i in range(self.dim):
            freq = 8 + 3 * np.sin(0.5 * i)
            amp = 1.2 + 0.8 * np.cos(0.3 * i)
            chaotic_mod += amp * np.sin(freq * np.pi * x[i]) * np.cos(freq * np.pi * x[i]) * np.exp(-0.2 * np.abs(x[i]))
        
        # Dynamic radial basis functions with time-varying centers and widths
        rbf = 0
        for i in range(self.dim):
            center = 1.5 * np.sin(0.7 * i + np.pi * self.dim / 4)
            width = 0.3 + 0.7 * np.cos(0.4 * i + np.pi * self.dim / 3)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Enhanced polynomial couplings with non-linear cross-dimensional interactions
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                poly_coupling += 0.4 * (x[i]**4) * (x[j]**3) * np.sin(np.pi * (x[i] + x[j])) * np.cos(0.5 * np.pi * (x[i] - x[j]))
        
        # Quaternion-inspired cross-dimensional interactions with dynamic phase shifts
        quat_interaction = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                phase_shift = 0.5 * np.sin(0.3 * i)
                quat_interaction += 0.5 * np.sin(np.pi * (x[i]**2 + x[i+1]**2) + phase_shift) * np.cos(np.pi * (x[i] * x[i+1]) + phase_shift)
        
        # Dynamic scaling and global shift with dimension-dependent factors
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1) + 0.1 * np.sin(0.2 * self.dim)
        shift = 0.8 * np.sum(np.abs(x)**1.7) + 0.2 * np.sum(x**4)
        
        # Novel adaptive noise component with multi-frequency modulation
        noise = 0.1 * np.sum(np.sin(15 * np.pi * x) ** 2 + np.cos(10 * np.pi * x) ** 2 + np.sin(20 * np.pi * x) ** 2)
        
        # Additional coupling term for enhanced non-separability
        coupling_term = 0
        for i in range(self.dim):
            if i + 2 < self.dim:
                coupling_term += 0.25 * (x[i] * x[i+1] * x[i+2]) * np.exp(-0.1 * (x[i]**2 + x[i+1]**2 + x[i+2]**2))
        
        # Combine all components
        return scale_factor * (sphere + 0.5 * chaotic_mod + 0.4 * rbf + 0.3 * poly_coupling + 0.25 * quat_interaction + coupling_term) + shift + noise