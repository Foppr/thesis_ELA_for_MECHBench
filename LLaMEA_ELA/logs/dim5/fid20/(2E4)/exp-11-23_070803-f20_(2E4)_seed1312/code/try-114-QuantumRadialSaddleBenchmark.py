import numpy as np

class QuantumRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Quantum harmonic oscillator component with dimensionally varying frequencies
        quantum_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Quantum-like potential with frequency modulation
            omega = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            quantum_component += 0.5 * omega**2 * xi**2 + 0.25 * xi**4
        
        # Radial basis function component with adaptive widths and centers
        radial_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple RBFs with varying widths and centers
            centers = np.linspace(-1, 1, 5)
            widths = 0.3 + 0.2 * np.sin(i * np.pi / self.dim)
            for center in centers:
                radial_component += np.exp(-0.5 * ((xi - center) / widths)**2)
        
        # Asymmetric hyperbolic tangent saddle potentials
        saddle_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Hyperbolic tangent potentials with asymmetric slopes
            slope1 = 1.0 + 0.3 * np.sin(i * np.pi / self.dim)
            slope2 = 0.7 + 0.3 * np.cos(i * np.pi / self.dim)
            saddle_component += (np.tanh(slope1 * xi) - np.tanh(slope2 * xi))**2
        
        # Adaptive coupling with dynamic interaction strengths
        coupling_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on dimension indices
                coupling_strength = 0.6 + 0.4 * np.sin((i + j) * np.pi / (self.dim + 1))
                coupling_component += coupling_strength * np.sin(np.pi * (x_norm[i] - x_norm[j]))**2
        
        # Dynamic noise modulation based on position
        noise_modulation = 0
        for i in range(self.dim):
            xi = x_norm[i]
            noise_modulation += 0.01 * np.sin(10 * xi) * np.cos(5 * xi)
        
        # Fractal-like dimensionality scaling with recursive structure
        fractal_component = 0
        for i in range(self.dim):
            xi = x_norm[i]
            # Recursive fractal component with diminishing returns
            scale = 1.0
            for k in range(3):
                scale *= 0.5
                fractal_component += scale * np.sin(2**(k+1) * xi)
        
        # Combined weighted sum of all components
        result = 1.5 * quantum_component + 1.0 * radial_component + 0.8 * saddle_component + \
                0.7 * coupling_component + 0.9 * fractal_component + noise_modulation
        
        # Add controlled dynamic noise
        noise = np.random.normal(0, 0.003 * (1 + 0.5 * np.abs(np.mean(x_norm))))
        
        return result + noise