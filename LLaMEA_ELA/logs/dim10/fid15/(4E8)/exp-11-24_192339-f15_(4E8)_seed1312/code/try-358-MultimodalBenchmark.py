import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal basin boundary components with chaotic dynamics
        fractal = 0
        for i in range(self.dim):
            # Chaotic logistic map based modulation
            chaos_param = 3.9 * (1.0 + 0.1 * np.sin(0.5 * x[i]))
            chaotic_term = np.sin(chaos_param * x[i] + np.pi/4) * np.cos(0.7 * x[i])
            # Fractal dimension modulation
            fractal_dim = 1.5 + 0.5 * np.sin(0.3 * x[i] + self.dim * 0.1)
            fractal += chaotic_term * np.exp(-fractal_dim * np.abs(x[i]))
        
        # Temporal coupling with memory effects and phase interference
        temporal = 0
        for i in range(self.dim):
            # Memory-based coupling with previous dimensions
            coupling = 0
            for j in range(max(0, i-3), i):
                coupling += np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(0.5 * (x[i] + x[j]))
            # Phase interference term
            phase = np.sin(0.4 * x[i] + self.dim * 0.3) * np.cos(0.6 * x[i])
            temporal += coupling * phase
        
        # Quantum interference patterns with dynamic superposition
        quantum = 0
        for i in range(self.dim):
            # Superposition of multiple wave functions
            wave1 = np.sin(x[i] + self.dim * 0.2) * np.exp(-0.1 * x[i]**2)
            wave2 = np.cos(0.8 * x[i] + self.dim * 0.3) * np.exp(-0.15 * x[i]**2)
            wave3 = np.sin(1.2 * x[i] + self.dim * 0.1) * np.exp(-0.05 * x[i]**2)
            # Interference pattern
            interference = (wave1 + wave2 + wave3)**2
            quantum += interference
        
        # Multi-scale ridge structures with varying curvature and orientation
        ridges = 0
        for i in range(self.dim):
            # Multiple ridge components with different orientations
            ridge1 = np.exp(-0.5 * ((x[i] - 1.0) / 0.8)**2) * np.sin(3.0 * x[i])
            ridge2 = np.exp(-0.5 * ((x[i] + 1.5) / 1.2)**2) * np.cos(2.0 * x[i])
            ridge3 = np.exp(-0.5 * ((x[i] - 2.5) / 0.6)**2) * np.sin(4.0 * x[i]**2)
            ridges += ridge1 + ridge2 + ridge3
        
        # Asymmetric multimodal structure with basin merging effects
        asymmetric = 0
        for i in range(self.dim):
            # Multiple local minima with varying depths
            min1 = np.exp(-0.5 * (x[i] - 1.0)**2) * (1.0 + 0.3 * np.sin(5.0 * x[i]))
            min2 = np.exp(-0.5 * (x[i] + 1.0)**2) * (1.0 + 0.4 * np.cos(4.0 * x[i]))
            min3 = np.exp(-0.5 * (x[i] - 3.0)**2) * (0.8 + 0.2 * np.sin(6.0 * x[i]))
            # Basin merging term
            merge = 0.1 * np.sin(2.0 * x[i]) * np.exp(-0.05 * (x[i] - 2.0)**2)
            asymmetric += min1 + min2 + min3 + merge
        
        # Dynamic conditioning with time-varying landscape features
        condition = 1.0 + 0.3 * np.sin(0.5 * self.dim) + 0.2 * np.cos(0.3 * x[0] if self.dim > 0 else 0)
        
        # Combine all components with optimized weights
        return condition * (0.25 * fractal + 0.20 * temporal + 
                           0.25 * quantum + 0.20 * ridges + 0.10 * asymmetric)