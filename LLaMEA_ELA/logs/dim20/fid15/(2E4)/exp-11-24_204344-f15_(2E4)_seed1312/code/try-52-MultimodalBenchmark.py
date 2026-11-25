import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Polynomial chaos component with varying exponents and coefficients
        poly_chaos = 0.0
        for i in range(self.dim):
            exp = 2 + (i % 5) * 0.5
            coeff = 1.5 + 0.5 * np.sin(i * 0.7)
            poly_chaos += coeff * np.abs(x[i])**exp
        
        # Radial basis function with multiple centers and varying widths
        rbf = 0.0
        centers = np.linspace(-4, 4, min(8, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)]
            width = 0.5 + 0.3 * np.cos(i * 0.5)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Quantum-inspired oscillation with phase modulation
        quantum = 0.0
        for i in range(self.dim):
            phase = 2 * np.pi * (i + 1) / self.dim
            freq = 3 + 2 * np.sin(i * 0.8)
            amp = 1.2 + 0.8 * np.cos(i * 0.6)
            quantum += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] * 0.3 + phase)
        
        # Cross-dimensional coupling with tensor products and trigonometric interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                cross_coupling += np.sin(x[i] * x[j]) * np.cos(2 * (x[i] + x[j])) * (1 + 0.1 * np.sin(i + j))
        
        # Asymmetric polynomial with multiple local minima
        asymmetric = 0.0
        for i in range(self.dim):
            asymmetric += 0.5 * (x[i]**3 - 3*x[i])**2 + 0.3 * np.sin(5 * x[i]) * np.cos(2 * x[i])
        
        # Multi-scale harmonic modulation with frequency-dependent amplitudes
        harmonic = 0.0
        for i in range(self.dim):
            freqs = [1, 2, 4, 8]
            for f in freqs:
                amp = 0.5 + 0.3 * np.sin(f * i)
                harmonic += amp * np.sin(f * x[i]) * np.cos(0.5 * f * x[i])
        
        # Basin structure with varying depths and widths
        basin_structure = 0.0
        for i in range(self.dim):
            basin_structure += 0.8 * (x[i] - 2)**4 + 0.4 * (x[i] + 1)**3 + 0.2 * np.cos(3 * x[i])
        
        # Combined scaling and offset to control overall landscape characteristics
        return 1.5 * (poly_chaos + rbf + quantum + cross_coupling + asymmetric + harmonic + basin_structure)