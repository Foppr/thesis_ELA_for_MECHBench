import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute graph Laplacian eigenvalues for spectral components
        self.laplacian_eigenvals = np.array([1.0 + i * 0.15 for i in range(dim)])
        # Fractal scaling parameters for adaptive potential wells
        self.fractal_params = np.array([0.5 + 0.3 * np.sin(i * 0.7) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillators with dynamic frequency modulation
        quantum = 0
        for i in range(self.dim):
            freq = 1.0 + 0.4 * np.sin(0.6 * x[i]) + 0.2 * np.cos(0.3 * x[i])
            oscillator = np.sin(freq * x[i]) * np.cos(freq * x[i]**2) * np.exp(-0.1 * x[i]**2)
            quantum += oscillator * (1.0 + 0.1 * np.sin(0.5 * x[i]))
        
        # Adaptive fractal potential wells with multi-scale coupling
        fractal = 0
        for i in range(self.dim):
            scale = self.fractal_params[i % len(self.fractal_params)]
            well = (x[i]**6 - 15*x[i]**4 + 75*x[i]**2 - 125) * np.exp(-0.08 * x[i]**2)
            fractal += well * np.sin(scale * x[i]) * np.cos(scale * x[i]**2)
        
        # Dynamic saddle-point modulation with chaotic coupling
        saddle = 0
        for i in range(self.dim):
            modulator = 1.0 + 0.3 * np.sin(0.4 * x[i]) * np.cos(0.6 * x[i])
            saddle += (x[i]**3 - 3*x[i]) * modulator * np.exp(-0.05 * x[i]**2)
        
        # Multi-scale ridge structures with torsion and curvature
        ridge = 0
        for i in range(self.dim):
            torsion = np.sin(0.4 * x[i]) * np.cos(0.8 * x[i])
            curvature = np.sin(0.3 * x[i]**2) * np.cos(0.7 * x[i]**2)
            ridge += torsion * curvature * (x[i]**4 - 4*x[i]**2 + 1) * np.exp(-0.1 * x[i]**2)
        
        # Enhanced basin coupling with quantum tunneling effects
        basin = 0
        for i in range(self.dim):
            threshold = 1.5 + 1.0 * np.sin(0.5 * x[i])
            tunneling = 0.1 * np.exp(-0.5 * (x[i] - threshold)**2)
            basin += ((x[i] > threshold) * (x[i]**3 - 3*x[i]) + 
                     (x[i] <= threshold) * (x[i]**2 - 1)) * tunneling
        
        # Emergent optimization patterns with evolutionary resonance
        evolution = 0
        for i in range(self.dim):
            resonance_freq = 1.0 + 0.5 * np.sin(0.7 * x[i])
            evolution += np.sin(resonance_freq * x[i]) * np.cos(resonance_freq * x[i]**3) * np.exp(-0.07 * x[i]**2)
        
        # Combine all components with dynamic weighting and chaotic modulation
        weights = [0.25, 0.20, 0.18, 0.15, 0.12, 0.08 + 0.03 * np.sin(0.4 * sum(x))]
        return (weights[0] * quantum + 
                weights[1] * fractal + 
                weights[2] * saddle + 
                weights[3] * ridge + 
                weights[4] * basin + 
                weights[5] * evolution)