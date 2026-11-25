import numpy as np

class QuaternionHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic frequencies and quaternion weights
        self.frequencies = 1.0 + 2.0 * np.sin(np.arange(dim) * np.pi / (dim + 1))
        self.quaternion_weights = np.array([1.0, 1.0j, 1.0+1.0j, 1.0-1.0j])[:dim%4 or 4] if dim > 3 else np.array([1.0, 1.0j])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical harmonics component with radial dependence
        spherical_harmonics = 0.0
        for i in range(self.dim):
            r = np.sqrt(np.sum(x**2))
            if r > 1e-8:
                theta = np.arccos(x[i] / r) if i < self.dim - 1 else 0.0
                phi = np.arctan2(x[i+1] if i+1 < self.dim else 0.0, x[i] if i < self.dim - 1 else 1.0)
                spherical_harmonics += (x[i]**2 + r**2) * np.sin(self.frequencies[i] * theta) * np.cos(self.frequencies[i] * phi)
        
        # Quaternion-inspired coupling with complex interactions
        quaternion_coupling = 0.0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                q_real = x[i]**2 - x[i+1]**2
                q_imag = 2 * x[i] * x[i+1]
                quaternion_coupling += np.sin(q_real) * np.cos(q_imag)
        
        # Quantum-like interference with phase modulation
        quantum_interference = 0.0
        for i in range(self.dim):
            phase = np.exp(1j * x[i] * self.frequencies[i])
            quantum_interference += np.real(phase * np.conj(phase)) * np.sin(x[i]**2)
        
        # Radial polynomial with fractional exponents
        radial_poly = 0.0
        for i in range(self.dim):
            radial_poly += (x[i]**(1.5 + i/10.0)) * np.cos(3.0 * x[i])
        
        # Cross-dimensional coupling with permutation symmetry
        cross_coupling = 0.0
        for i in range(self.dim - 2):
            j, k = i+1, i+2
            if j < self.dim and k < self.dim:
                cross_coupling += np.sin(x[i] * x[j]) * np.cos(x[j] * x[k])
        
        # Logarithmic spiral with complex amplitude modulation
        log_spiral = 0.0
        for i in range(self.dim):
            r = np.sqrt(x[i]**2 + 1e-8)
            angle = np.arctan2(x[i], 1.0)
            log_spiral += r * np.cos(angle * (i + 1)) * np.sin(r * (i + 1))
        
        # Fractal dimensionality scaling with recursive pattern
        fractal_scale = 1.0 + 0.5 * np.sin(np.log(self.dim + 1))
        
        # Combined function with adaptive weights
        return fractal_scale * (0.7 * spherical_harmonics + 0.6 * quaternion_coupling + 
                               0.5 * quantum_interference + 0.4 * radial_poly + 
                               0.3 * cross_coupling + 0.2 * log_spiral)