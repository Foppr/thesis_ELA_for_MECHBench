import numpy as np

class QuantumChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quantum-inspired frequencies and chaos parameters
        self.frequencies = np.array([1.0 + 0.5 * np.sin(i * 0.7) for i in range(dim)])
        self.chaos_params = np.array([0.3 + 0.4 * np.cos(i * 0.5) for i in range(dim)])
    
    def f(self, x):
        x = np.array(x)
        
        # Quantum-inspired oscillatory terms with complex phase modulation
        quantum_term = 0.0
        for i in range(self.dim):
            phase = self.frequencies[i] * x[i] + np.sin(x[i] * 0.5) * np.cos(x[i] * 0.3)
            amplitude = 1.0 + 0.3 * np.sin(x[i] * 0.7)
            quantum_term += amplitude * np.sin(phase) * np.cos(phase * 0.6) * np.exp(-0.1 * x[i]**2)
        
        # Polynomial chaos expansion with Hermite polynomials
        chaos_poly_term = 0.0
        for i in range(self.dim):
            xi = (x[i] - np.mean(x)) / (np.std(x) + 1e-8)
            # Third-order Hermite polynomial: H3(x) = 8x^3 - 12x
            h3 = 8 * xi**3 - 12 * xi
            chaos_poly_term += h3 * np.exp(-0.5 * xi**2) * self.chaos_params[i]
        
        # Adaptive penalty terms with dynamic thresholds
        penalty_term = 0.0
        for i in range(self.dim):
            # Dynamic threshold based on dimensionality and position
            threshold = 2.0 + 1.5 * np.sin(i * 0.4 + self.dim * 0.3)
            distance_from_threshold = np.abs(x[i] - threshold)
            penalty_term += 0.5 * distance_from_threshold**2 * (1.0 + 0.2 * np.sin(x[i] * 0.8))
        
        # Rugged landscape with multiple interacting peaks and valleys
        rugged_term = 0.0
        for i in range(self.dim):
            # Multi-peak structure with varying heights and widths
            peak_heights = [1.0, 2.5, 1.8, 3.2]
            peak_positions = [-3.0, -1.0, 1.0, 3.0]
            peak_widths = [0.5, 1.0, 0.7, 1.2]
            
            for h, p, w in zip(peak_heights, peak_positions, peak_widths):
                rugged_term += h * np.exp(-0.5 * ((x[i] - p) / w)**2)
        
        # Coupling terms with quantum entanglement-inspired interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quantum-like coupling with phase interference
                coupling_phase = np.sin(x[i] * x[j] * 0.3) + np.cos(x[i] + x[j] * 0.2)
                coupling_strength = 0.5 + 0.3 * np.sin(i * j * 0.1)
                coupling_term += coupling_strength * coupling_phase * (x[i]**2 + x[j]**2)
        
        # Adaptive conditioning factor with chaotic modulation
        conditioning_factor = 1.0 + 0.4 * np.sin(self.dim * 0.5) * np.cos(self.dim * 0.2)
        
        # Final combination of all terms
        total = 0.3 * quantum_term + 0.25 * chaos_poly_term + 0.2 * penalty_term + \
                0.15 * rugged_term + 0.1 * coupling_term
        
        return total * conditioning_factor