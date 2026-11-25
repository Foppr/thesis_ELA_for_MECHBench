import numpy as np

class HyperChaoticEntangledBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Quantum-like superposition radial term with phase interference
        r_squared = np.sum(x**2)
        quantum_radial = np.exp(-0.15 * r_squared) * np.cos(r_squared * 0.5) * (r_squared + 1e-8)
        
        # Memetic evolution landscape with adaptive fitness landscapes
        memetic_term = 0.0
        for i in range(self.dim):
            # Adaptive fitness landscape based on position
            adaptive_factor = 1.0 + 0.3 * np.sin(x[i] * np.pi / 2)
            memetic_term += (x[i]**4 - 6*x[i]**2 + 9) * adaptive_factor
        
        # Non-local entanglement interactions with long-range coupling
        entanglement_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                # Non-local coupling with quantum-like phase factor
                phase = np.sin(dist * np.pi / (self.dim + 1))
                entanglement_term += (x[i]**2 + x[j]**2) * np.exp(-0.3 * dist) * phase
        
        # Hyper-chaotic local minima with multi-scale tunneling effects
        tunneling_minima = 0.0
        for i in range(self.dim):
            # Multi-scale potential wells with varying depths and positions
            center = 2.5 * np.sin(i * np.pi / (self.dim + 2)) * np.cos(i * np.pi / (self.dim + 4))
            depth = 1.5 + 0.8 * np.sin(i * np.pi / (self.dim + 3))
            width = 0.5 + 0.3 * np.cos(i * np.pi / (self.dim + 5))
            tunneling_minima += depth * np.exp(-((x[i] - center)**2) / (2 * width**2)) * (x[i]**8 - 4*x[i]**6 + 6*x[i]**4 - 4*x[i]**2 + 1)
        
        # Quantum tunneling and resonance effects
        resonance_term = 0.0
        for i in range(self.dim):
            resonance_term += np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 2)) * np.exp(-0.2 * x[i]**2)
        
        # Hyper-chaotic symmetry breaking with delayed feedback
        symmetry_breaking = 0.0
        for i in range(self.dim):
            delay_idx = (i + self.dim//4) % self.dim
            symmetry_breaking += np.sin(x[i] * 2) * np.cos(x[delay_idx] * 1.5) * np.tan(x[i] / (i + 3))
        
        # Multi-dimensional fractal-like structure with self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(x[i] * 2**i) * np.cos(x[i] * 3**i) * (1 + 0.1 * np.sin(i * np.pi / self.dim))
        
        # Dimensionality-dependent chaotic scaling with quantum correction
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / 6) + 0.05 * np.cos(self.dim * np.pi / 3)
        
        # Combine all terms with optimized weights for maximum difficulty
        return dim_factor * (0.2 * quantum_radial + 
                            0.2 * memetic_term + 
                            0.2 * entanglement_term + 
                            0.15 * tunneling_minima + 
                            0.1 * resonance_term + 
                            0.1 * symmetry_breaking + 
                            0.05 * fractal_term)