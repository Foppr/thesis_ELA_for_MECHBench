import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic components with hyperchaotic modulation
        quantum_harmonic = 0
        for i in range(self.dim):
            freq = 2.1 + 1.2 * np.sin(1.3 * x[i] + self.dim * 0.4 + 0.5 * np.sin(x[i]**2))
            phase = 1.1 * np.cos(1.2 * x[i] + 0.6 * self.dim + 0.3 * np.sin(x[i]) + 0.2 * np.cos(x[i]**2))
            quantum_harmonic += freq * (x[i]**2) * np.exp(-0.3 * x[i]**2) * np.cos(phase)
        
        # Dynamic fractal RBF ensemble with chaotic center positioning
        rbf_ensemble = 0
        for i in range(self.dim):
            width = 2.0 + 0.8 * np.sin(1.1 * x[i] + self.dim * 0.3 + 0.4 * np.cos(x[i]))
            center = 4.0 * np.cos(1.0 * x[i] + self.dim * 0.5 + 0.25 * np.sin(x[i]**2) + 0.1 * np.cos(x[i]))
            rbf_ensemble += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Hyperchaotic spectral filter with multi-frequency coupling
        spectral_filter = 0
        for i in range(self.dim):
            freq_mod = 2.3 + 1.0 * np.sin(0.8 * x[i] + self.dim * 0.35 + 0.6 * np.cos(x[i]) + 0.4 * np.sin(x[i]**2))
            spectral_filter += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]**3) * np.exp(-0.15 * x[i]**2)
        
        # Dynamic scaling with hyperbolic conditioning
        conditioning = 2.0 + 0.8 * np.sin(self.dim * 0.7) + 0.6 * np.cos(self.dim * 0.8) + 0.4 * np.tanh(self.dim * 0.1)
        
        # Enhanced cross-dimensional coupling with quantum phase interaction
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                poly_term = (x[i]**2 + x[j]**2) * np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(0.7 * (x[i] + x[j]) + 0.3 * np.cos(x[i]*x[j]))
                cross_coupling += poly_term
        
        # Hyper-multimodal structure with asymmetric chaotic trigonometric combinations
        multimodal_structure = 0
        for i in range(self.dim):
            term1 = np.sin(4.0 * x[i]) * np.cos(5.0 * x[i]**2)
            term2 = np.sin(3.5 * x[i]**3) * np.cos(4.5 * x[i])
            term3 = np.sin(2.5 * x[i]) * np.cos(3.5 * x[i]**3)
            term4 = np.sin(1.5 * x[i]**2) * np.cos(2.5 * x[i]**2)
            multimodal_structure += term1 + term2 + term3 + term4
        
        # Fractal-based adaptive weights with hyperbolic scaling
        fractal_weight = 1.8 + 0.6 * np.sin(self.dim * 0.85 + 0.3 * np.cos(x[0] if self.dim > 0 else 0) + 0.2 * np.sin(x[0]**2))
        
        # Combine all components with enhanced weights for maximum challenge
        return conditioning * fractal_weight * (0.4 * quantum_harmonic + 0.25 * rbf_ensemble + 
                              0.2 * spectral_filter + 0.1 * cross_coupling + 0.05 * multimodal_structure)